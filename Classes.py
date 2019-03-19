import cv2 as cv
import numpy as np

# TODO comprobar que """ ... """ se puede leer cuando se hace help(filecreator), por ejemplo
# TODO comprobar que """ ... """ funciona para clases
# TODO incluir en el readme e instrucciones del codigo que help(funcion) y help(class) funcionan

class ImageTreatment:
""" Umbralizes and cleans the frames to make easier to locate moving objects """

    @staticmethod
    def mean(background, frame):
        """ substracts an image stated as background and supposes the remaining to be moving objects"""
		background = cv.cvtColor(background, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        background = background.astype('double')
        frame = frame.astype('double')

        imres = np.abs(np.array(frame) - np.array(background))

        imres = imres.astype('uint8')
		# we umbralise the moving objects to work with a boolean matrix
        imres[imres < 110] = 0
        imres[imres > 111] = 255
		# returns a (0-255) boolean matrix, being white the moving people
        return imres

    @staticmethod
    def clean(frame):
		""" the frame called should be of type boolean matrix (specifically, the return of mean())"""
        frame = cv.erode(frame, (9, 9), iterations=4)
        frame = cv.dilate(frame, (9, 9), iterations=4)
        imres = cv.GaussianBlur(frame, (5, 13), 0)
        # cleans the entered image
		return imres


class FindAndFollow:
"""Detects objects moving and counts when they go through certain areas"""

    @staticmethod
    def detect(image):
        """ given a boolean image, creates contours arround true (white) objects"""
		data = []
        _, cont, _ = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        if len(cont) != 0:
            c = max(cont, key= cv.contourArea)
            (x, y), radius = cv.minEnclosingCircle(c)
            # here a humble approximation of a person form (rectangle) and feet position (data)
			if radius > 14:
                # cv.circle(image, (int(x), int(y)), int(radius), 255, 2)
                cv.rectangle(image, (int(x-10), int(y-20)), (int(x+10), int(y+20)), 255, 2)
                data.append([int(x), int(y+20)])
		# returns the bottom of the contours created
		# this bottom points are supposed to be feet of moving people (taken as reference)
        return image, data

    @staticmethod
    def follow(data):
        """ cross increases in case data (feet) crosses the door area"""
		cross = 0
        nocross = 0
        while len(data) > 0:
            aux = data.pop()
			# door area:
            if 210 < aux[0] < 330 and 140 < aux[1] < 160:
                cross += 1
            else:
                nocross += 1
		# returns the number of people inside the door area in the current frame
        return cross, nocross


class InOut:
""" Video and report_file management"""

    @staticmethod
    def filecreator():
        """ creates a file where data of the video will be stored"""
		try:
            fileData = open("results.csv", "w")
        except AttributeError:
            print("Couldn't create data {}".format())
        return fileData

    @staticmethod
    def videoin(arg):
		"""opens the video to be analyzed"""
        path = arg["video"]
        videoInput = cv.VideoCapture(path)
        if not videoInput.isOpened():
            print("Error during video load.")

        _, imagepast = videoInput.read()
        return videoInput, imagepast

    @staticmethod
    def printer(filedata, c, noc, frame):
        """ writes an information line per frame on the csv """
		filedata.write("Frame: " + str(frame) + ". People in image: " + str(noc) + ", People crossing: " + str(c) + "\r\n")
        return

