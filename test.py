import unittest
import cv2 as cv

class TestStringMethods(unittest.TestCase):
    def test_CamIn(self):
        self.assertTrue(functions.CameraIn("video.avi"))
        
        
    def test_OutStore(self):
        self.assertTrue(functions.In_Store(10, 480, 70, 100))
        self.assertFalse(functions.In_Store(100, 480, 400, 1000))
    def test_Detect(self):
        imgBW = cv.imread("image_background.jpg")
        imgNew = cv.imread("image_new.jpg")
        self.assertTrue(functions.Detect(imgBW, imgNew))
