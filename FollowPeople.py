import cv2 as cv
import argparse

from AppsIndustriales import Classes


ap = argparse.ArgumentParser()
ap.add_argument("-video", required=True, help="Path of the video.")
args = vars(ap.parse_args())

Io = Classes.InOut()
It = Classes.ImageTreatment()
Ff = Classes.FindAndFollow()

fileData = Io.filecreator()
videoInput, imagepast = Io.videoin(args)

while videoInput.isOpened():

    ret, image = videoInput.read()
    img = It.mean(imagepast, image)
    img = It.clean(img)
    img, data = Ff.detect(img)
    c, noc = Ff.follow(data)

    Io.printer(fileData, c, noc, int(videoInput.get(1)))
    cv.imshow("Frame", img)
    cv.waitKey(22)

videoInput.release()
fileData.close()
cv.destroyAllWindows()
