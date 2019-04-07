from Classes import FindAndFollow
import unittest
# import cv2

print("hello world")
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')


class TestStringMethods(unittest.TestCase):
    """Module to test the proper work of AIVA-Store_Entrance program"""

    def test_detect(self):
        self.assertTrue(FindAndFollow.detect(image=cv2.imread("./test_detected")))

    # def test_initialization(self):
    #     self.assertEqual(FindAndFollow.follow(), 0)
    #     print("alright")


if __name__ == '__main__':
    unittest.main()
