# Detecção de pessoas (em pé)

# Camera online abertas: http://www.insecam.org/en/
# Priorizar cameras modelo AXIS para ter mais garantia de formato 'mjpg'
# Link da camera (NY1): http://www.insecam.org/en/view/973842/
# Link da camera (NY2): http://www.insecam.org/en/view/911230/

import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('http://108.30.103.58:8082/mjpg/video.mjpg?size=1')
# Usando camera publica 1 de NY


#cap = cv2.VideoCapture('http://72.43.190.171:81/mjpg/video.mjpg?size=1')
# Usando camera publica 2 de NY

if not cap.isOpened():
    # Verifica se alguma camera esta sendo detectada
    print('Nenhuma camera aberta')
    exit()

windowName = 'CAM 1'

# Dimensões da gravação(Usando as mesmas resoluções do video original):
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec:
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# Saida:
out = cv2.VideoWriter('takes/saida.mp4', fourcc, 7.0, (width, height))

while True:
    ret, frame = cap.read()
    # Variavel 'ret' usada para fazer a verificação da chegada do frame


    if not ret:
        # Veriifiica se algum frama esta sendo cappturado
        print('Nenhum frame capturado')
        break
    
    # Detecção de pessoas:
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))

    frame = cv2.putText(frame, 'Camera 01', (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
    # (50,50) = posição do texto | FONT = estilo fonte | 2 = modelo fonte | (0,0,0) = cor | 3 = espessura letras

    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow(windowName, frame)

    out.write(frame)

    # Execução da camrea:
    k = cv2.waitKey(1)  # 1 milisegundo. 0 ira deixa-lo parado esperando eternamente
        # waitKey retorna qual tecla foi apertada

    if k == ord('q'):
        break

    if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
        # Possibiilita fechar o propgrama apenas clicando no "X"
        break

cv2.destroyAllWindows()
cap.release()
out.release()
print('Camera encerrada')
