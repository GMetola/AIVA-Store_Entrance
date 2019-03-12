import cv2
from pathlib import Path

path = Path('./EnterExitCrossingPaths1front.mpg')

cap = cv2.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read()

# TODO Sólo hay que hacer diagramas para la aplicación de visión
# TODO Codificar la imagen antes de mandarla a internet. pg 19 del tema 5
# TODO Pruebas con imagenes de cuatro pixeles (255, 0, 0, 128)--> pag 15 del tema 5