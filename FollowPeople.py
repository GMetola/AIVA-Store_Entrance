import cv2 as cv
import argparse

import Classes

if __name__ == "__main__":

	ap = argparse.ArgumentParser()
	ap.add_argument("-video", required=True, help="Path of the video.")
	args = vars(ap.parse_args())

	# we create the objects defined on "Classes"
	Io = Classes.FileInOut()
	It = Classes.ImageTreatment()
	Ff = Classes.FindAndFollow()
	Vd = Classes.VideoData()

	fileData = Io.filecreator()
	videoInput, imagepast = Vd.videoin(args)

	while videoInput.isOpened():

		ret, image = videoInput.read()
		if not ret:
			break
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
