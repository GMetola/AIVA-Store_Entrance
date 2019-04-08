import Classes
import unittest
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')


class TestStringMethods(unittest.TestCase):
	"""Module to test the proper work of AIVA-Store_Entrance program"""

	def test_import(self):
		""" Test that the cv2 module can be imported. """
		import cv2 as cv

	def test_detect(self):
		import cv2 as cv
		self.assertTrue(FindAndFollow.detect(image=cv.imread("./test_detected.jpg")))

	# def test_initialization(self):
	#     self.assertEqual(FindAndFollow.follow(), 0)
	#     print("alright")

	def test_video_capture(self):

		import cv2 as cv
		cap = cv.VideoCapture("EnterExitCrossingPaths1front.mpg")
		self.assertTrue(cap.isOpened())

	def test_videoin(self):
		import cv2 as cv
		viddata = Classes.VideoData()
		viddata.videoin()
		cap = cv.VideoCapture("EnterExitCrossingPaths1front.mpg")
		self.assertTrue(cap.isOpened())
		
	def test_follow(self):
		self.assertEqual(FindAndFollow.follow(self, 0), [0,0])


if __name__ == '__main__':
    unittest.main()
