import cv2 as cv
import argparse
import numpy as np


class StoreDetection:
    def __init__(self):
        self.ap = ap
        self.path_in = path_in
        self.args = args
        self.args_in = args_in
        self.background = background
        self.frame = frame
        self.filtered = filtered
        self.movement = movement
        self.people = people

    def open_video(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-video", required=True, help="Path of the video.")
        args = vars(ap.parse_args())
        path_in = args["video"]
        return path_in, ap

    def mean(self):
        background = cv.cvtColor(self.background, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        background = background.astype('double')
        frame = frame.astype('double')

        movement = np.abs(np.array(frame) - np.array(background))

        movement = movement.astype('uint8')
        movement[movement < 110] = 0
        movement[movement > 111] = 255
        return self.movement

    def filter(self):
        frame = cv.erode(self.frame, (9, 9), iterations=4)
        frame = cv.dilate(frame, (9, 9), iterations=4)
        filtered = cv.GaussianBlur(frame, (5, 13), 0)
        return filtered

    def detect(self):
        people = []
        _, cont, _ = cv.findContours(self.frame, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        if len(cont) != 0:
            c = max(cont, key=cv.contourArea)
            (x, y), radius = cv.minEnclosingCircle(c)
            if radius > 14:
                # cv.circle(frame, (int(x), int(y)), int(radius), 255, 2)
                cv.rectangle(frame, (int(x-10), int(y-20)), (int(x+10), int(y+20)), 255, 2)
                people.append([int(x), int(y+20)])

        return frame, people

    def follow(self):
        cross = 0
        no_cross = 0
        while len(self.people) > 0:
            aux = self.people.pop()
            # goes though the store's door
            if 210 < aux[0] < 330 and 140 < aux[1] < 160:
                cross += 1
            else:
                no_cross += 1

        return cross, no_cross


class FileData(self):
    def __init__(self):
        self.frame = frame
        self.c = c
        self.noc = noc

    def printer(self):
        self.fileData.write("Frame: " + str(self.frame) + ". People in image: " +
                            str(self.noc) + ", People crossing: " + str(self.c) + "\r\n")
        return


if __name__ == '__main__':

    try:
        fileData = open("results.csv", "w")
    except AttributeError:
        print("Couldn't create data {}".format())

    videoInput = cv.VideoCapture(pathIn)
    if not videoInput.isOpened():
        print("Error during video load.")

    ret, past_image = videoInput.read()
    while videoInput.isOpened():

        ret, image = videoInput.read()
        if not ret:
            break

        img = mean(past_image, image)
        img = filter(img)
        img, data = detect(img)
        c, noc = follow(data)
        printer(fileData, c, noc, int(videoInput.get(1)))
        cv.imshow("Frame", img)
        cv.waitKey(22)

    videoInput.release()
    fileData.close()
    cv.destroyAllWindows()
