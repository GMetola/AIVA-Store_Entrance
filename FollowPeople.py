import cv2 as cv
import argparse
import numpy as np


def mean(imagepast, image):
    imagepast = cv.cvtColor(imagepast, cv.COLOR_BGR2GRAY)
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    imagepast = imagepast.astype('double')
    img = img.astype('double')

    imagefin = np.abs(np.array(img) - np.array(imagepast))

    imagefin = imagefin.astype('uint8')
    imagefin[imagefin < 110] = 0
    imagefin[imagefin > 111] = 255
    return imagefin


def filt(image):
    image = cv.erode(image, (9, 9), iterations=4)
    image = cv.dilate(image, (9, 9), iterations=4)
    imagefin = cv.GaussianBlur(image, (5, 13), 0)
    return imagefin


def detect(image):
    data = []
    _, cont, _ = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    if len(cont) != 0:
        c = max(cont, key= cv.contourArea)
        (x, y), radius = cv.minEnclosingCircle(c)
        if radius > 14:
            # cv.circle(image, (int(x), int(y)), int(radius), 255, 2)
            cv.rectangle(image, (int(x-10), int(y-20)),(int(x+10), int(y+20)), 255, 2)
            data.append([int(x), int(y+20)])

    return image, data


def follow(data):
    cross = 0
    noCross = 0
    while len(data) > 0:
        aux = data.pop()
        # goes though the store's door
        if aux[0] > 210 and aux[0] < 330 and aux[1] > 140 and aux[1] < 160:
            cross = cross + 1
        else:
            noCross = noCross+1

    return cross, noCross


def printer(fileData, c, noc, frame):
    fileData.write("Frame: " + str(frame) + ". People in image: " + str(noc) + ", People crossing: " + str(c) + "\r\n")
    return


ap = argparse.ArgumentParser()
ap.add_argument("-video", required=True, help="Path of the video.")
args = vars(ap.parse_args())
pathIn = args["video"]

try:
    fileData = open("results.csv", "w")
except AttributeError:
    print("Couldn't create data {}".format())


videoInput = cv.VideoCapture(pathIn)
if not videoInput.isOpened():
    print("Error during video load.")


ret, imagepast = videoInput.read()
while videoInput.isOpened():

    ret, image = videoInput.read()
    img = mean(imagepast, image)
    img = filt(img)
    img, data = detect(img)
    c, noc = follow(data)

    printer(fileData, c, noc, int(videoInput.get(1)))
    cv.imshow("Frame", img)
    cv.waitKey(22)

videoInput.release()
fileData.close()
cv.destroyAllWindows()
