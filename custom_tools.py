from typing import Type, Optional
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

import cv2, time, os

class DetectInput(BaseModel):
    camera_url: Optional[str] = Field(
        #default='http://72.43.190.171:81/mjpg/video.mjpg?size=1',
        # default='http://108.30.103.58:8082/mjpg/video.mjpg?size=1',
        default=0,
        description='URL da camera MJPEG'
    )

class VideoTool(BaseTool):
    name: str = "Video Tool"
    description: str = "Monitora cameras em até N frames de uma MJPEG stream."
    args_schema: Type[BaseModel] = DetectInput

    # parâmetros internos
    max_frames: int = 150        # p.ex. ~20 s se a câmera manda 7 fps
    output_dir: str = "takes"     # onde salvar vídeo se quiser

    def _run(self, camera_url: str | None) -> str:
        print('DEBUG - cam url:', repr(camera_url))
        #hog = cv2.HOGDescriptor()
        #hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return "Não foi possível abrir a câmera."

        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  or 640)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        # garante que o diretório exista (OPCIONAL)
        #os.makedirs(self.output_dir, exist_ok=True)
        out_path = os.path.join(self.output_dir, f"detect_{int(time.time())}.mp4")
        out = cv2.VideoWriter(out_path, fourcc, 7.0, (width, height))

        total_people, frames_proc = 0, 0

        while frames_proc < self.max_frames:
            ok, frame = cap.read()
            if not ok:
                break

            #boxes, _ = hog.detectMultiScale(frame, winStride=(8, 8))

            # contabiliza pessoas detectadas
            #total_people += len(boxes)

            # desenha bounding‑boxes verdes
            #for (x, y, w, h) in boxes:
            #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            out.write(frame)
            frames_proc += 1

        cap.release()
        out.release()

        # resumo para o LLM
        return (
            #f"Processados {frames_proc} frames da câmera.\n"
            #f"Foram detectadas {total_people} pessoas no total.\n"
            f"Vídeo anotado salvo em: {out_path}"
        )