import cv2 as cv
import numpy as np


class ImageTreatment:

    @staticmethod
    def mean(background, frame):
        background = cv.cvtColor(background, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        background = background.astype('double')
        frame = frame.astype('double')

        imres = np.abs(np.array(frame) - np.array(background))

        imres = imres.astype('uint8')
        imres[imres < 110] = 0
        imres[imres > 111] = 255
        return imres

    @staticmethod
    def clean(frame):
        frame = cv.erode(frame, (9, 9), iterations=4)
        frame = cv.dilate(frame, (9, 9), iterations=4)
        imres = cv.GaussianBlur(frame, (5, 13), 0)
        return imres


class FindAndFollow:

    @staticmethod
    def detect(image):
        data = []
        _, cont, _ = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        if len(cont) != 0:
            c = max(cont, key= cv.contourArea)
            (x, y), radius = cv.minEnclosingCircle(c)
            if radius > 14:
                # cv.circle(image, (int(x), int(y)), int(radius), 255, 2)
                cv.rectangle(image, (int(x-10), int(y-20)), (int(x+10), int(y+20)), 255, 2)
                data.append([int(x), int(y+20)])

        return image, data

    @staticmethod
    def follow(data):
        cross = 0
        nocross = 0
        while len(data) > 0:
            aux = data.pop()
            if aux[0] > 210 and aux[0] < 330 and aux[1] > 140 and aux[1] < 160:
                cross = cross + 1
            else:
                noCross = nocross+1

        return cross, nocross


class InOut:

    @staticmethod
    def filecreator():
        try:
            fileData = open("results.csv", "w")
        except AttributeError:
            print("Couldn't create data {}".format())
        return fileData

    @staticmethod
    def videoin(arg):
        path = arg["video"]
        videoInput = cv.VideoCapture(path)
        if not videoInput.isOpened():
            print("Error during video load.")

        _, imagepast = videoInput.read()

        return videoInput, imagepast

    @staticmethod
    def printer(filedata, c, noc, frame):
        filedata.write("Frame: " + str(frame) + ". People in image: " + str(noc) + ", People crossing: " + str(c) + "\r\n")
        return

