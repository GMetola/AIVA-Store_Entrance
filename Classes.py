import cv2 as cv
import numpy as np


class ImageTreatment:
    """Umbralizes and cleans the frames to make easier to locate moving objects """

    def __init__(self):
        return

    @staticmethod
    def mean(background, frame):
        """ Substracts an image stated as background and supposes the remaining to be moving objects"""
        background = cv.cvtColor(background, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        background = background.astype('double')
        frame = frame.astype('double')

        imres = np.abs(np.array(frame) - np.array(background))

        imres = imres.astype('uint8')
        """we umbralize the moving objects to work with a boolean matrix"""
        imres[imres < 110] = 0
        imres[imres > 111] = 255
        """returns a (0-255) boolean matrix, being white the moving people"""
        return imres

    @staticmethod
    def clean(frame):
        """ the frame called should be of type boolean matrix (specifically, the return of mean())"""
        frame = cv.erode(frame, (9, 9), iterations=4)
        frame = cv.dilate(frame, (9, 9), iterations=4)
        imres = cv.GaussianBlur(frame, (5, 13), 0)
        """cleans the entered image"""
        return imres


class FindAndFollow:
    """Detects objects moving and counts when they go through certain areas"""

    __datacross = 0
    __lastcountdatacross = 0
    __datanocross = 0
    __lastcountdatanocross = 0

    def __init__(self):
        return

    @staticmethod
    def detect(image,imageOriginal):
        """ given a boolean image, creates contours arround true (white) objects"""
        data = []
        _, cont, _ = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        cnt = sorted(cont, key=cv.contourArea)

        while len(cnt) != 0:
            c = cnt.pop()
            (x, y), radius = cv.minEnclosingCircle(c)
            # here a humble approximation of a person form (rectangle) and feet position (data)

            if radius > 12:
                cv.rectangle(imageOriginal, (int(x-10), int(y-30)), (int(x+10), int(y+20)), 255, 2)
                data.append([int(x), int(y+20)])
            else:
                break
        """returns the bottom of the contours created.
        this bottom points are supposed to be feet of moving people (taken as reference)"""
        return imageOriginal, data

    def follow(self, data):
        """ cross increases in case data (feet) crosses the door area"""
        cross = 0
        no_cross = 0
        while len(data) > 0:
            aux = data.pop()
            # door area:
            if 210 < aux[0] < 330 and 140 < aux[1] < 160:
                cross += 1
            else:
                no_cross += 1

        if cross > 0 and self.__datacross < cross:
            self.__datacross = cross
            self.__lastcountdatacross = 0
        elif cross > 0 and self.__lastcountdatacross > 15:
            self.__datacross = self.__datacross + 1
            self.__lastcountdatacross = 0
        elif cross == 0:
            self.__lastcountdatacross = self.__lastcountdatacross + 1

        if no_cross > 0 and self.__datanocross < no_cross:
            self.__datanocross = no_cross
            self.__lastcountdatanocross = 0
        elif no_cross > 0 and self.__lastcountdatanocross > 15:
            self.__datanocross = self.__datanocross + 1
            self.__lastcountdatanocross = 0
        elif no_cross == 0:
            self.__lastcountdatanocross = self.__lastcountdatanocross + 1

            """returns the number of people inside the door area in the current frame"""
        return cross, no_cross

    def finalreport(self, filedata, inputoutput):

        inputoutput.printer(filedata, self.__datacross, self.__datanocross, "Final")
        return


class FileInOut:
    """ Report_file management"""


    def __init__(self):
        return

    @staticmethod
    def filecreator():
        """ creates a file where data of the video will be stored"""
        try:
            fileData = open("results10.csv", "w")
        except AttributeError:
            print("Couldn't create data {}".format())
        return fileData

    @staticmethod
    def printer(filedata, c, noc, frame):
        """ writes an information line per frame on the csv """
        filedata.write("Frame: " + str(frame) + ". People in image: "
                       + str(noc) + ", People crossing: " + str(c) + "\r\n")

        return


class VideoData:
    """Video file management"""

    def __init__(self):
        return

    @staticmethod
    def videoin(arg):
        """opens the video to be analyzed"""
        path = arg["video"]
        video_input = cv.VideoCapture(path)
        if not video_input.isOpened():
            print("Error during video load.")

        _, imagepast = video_input.read()
        return video_input, imagepast


