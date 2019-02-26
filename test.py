import functions
import unittest
import cv2

class TestStringMethods(unittest.TestCase):
    def test_CamIn(self):
        self.assertTrue(functions.CameraIn("video.avi"))     
      
    def test_OutStore(self):
        self.assertTrue(functions.In_Store(10, 480, 70, 100))
        self.assertFalse(functions.In_Store(100, 480, 400, 1000))
        print("alright")

    def test_Detect(self):
        imgBW = cv2.imread('image_background.jpg', 0)
        imgNew = cv2.imread("image_new.jpg", 0)
        self.assertTrue(functions.Detect(imgBW, imgNew))

if __name__ == '__main__':
    unittest.main()
