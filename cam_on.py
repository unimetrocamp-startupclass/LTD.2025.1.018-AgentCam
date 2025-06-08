# FUNCIONANDO
# cmake

# Camera online abertas: http://www.insecam.org/en/
# Link da camera que esta sendo usada no treino: http://www.insecam.org/en/view/1010700/

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Camera 0 é a webcam do pc (deafult)
# CAP_DSHOW tira o delay da abertura da camera

#cap = cv2.VideoCapture('http://103.95.42.254:84/mjpg/video.mjpg?camera=1&size=1')
# Usando camera publica para treino
# Priorizar cameras modelo AXIS para ter mais garantia de formato 'mjpg'

if not cap.isOpened():
    # Verifica se alguma camera esta sendo detectada
    print('Nenhuma camera aberta')
    exit()

windowName = 'CAM 1'

while True:
    ret, frame = cap.read()
    # Variavel 'ret' usada para fazer a verificação da chegada do frame

    if not ret:
        # Veriifiica se algum frama esta sendo cappturado
        print('Nenhum frame capturado')
        break

    frame = cv2.putText(frame, 'Camera 01', (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
    # (50,50) = posição do texto | FONT = estilo fonte | 2 = modelo fonte | (0,0,0) = cor | 3 = espessura letras

    cv2.imshow(windowName, frame)

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
print('Camera encerrada')







# Exemplo de modificações possiveis:

# - Transformação da imagem em escala b/w:
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)