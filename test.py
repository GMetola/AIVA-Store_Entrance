from Classes import FindAndFollow
import FollowPeople
import unittest
import cv2


class TestStringMethods(unittest.TestCase):
    """Module to test the proper work of AIVA-Store_Entrance program"""

    def test_detect(self):
        self.assertTrue(FindAndFollow.detect(image=cv2.imread("./test_detected")))

    # def test_initialization(self):
    #     self.assertEqual(FindAndFollow.follow(), 0)
    #     print("alright")


if __name__ == '__main__':
    unittest.main()
