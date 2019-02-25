import numpy as np
import cv2 as cv


def CameraIn(data):
  if not data:
    return False
  else:
    return True
  
def CameraOut():
  return True

def In_Store(x, y, h, w):
  
  if (x+h) < 342 and (y+w) > 520 and (y+w) < 883:
    return True
  else:
    return False

def Out_Store(x, y, h, w):
  
  if (x+h) > 342 or (y+w) < 520 or (y+w) > 883:
    return True
  else:
    return False 
  
def Detect(img_bw, img):
  imgBW = cv.cvtColor(img_bw, cv.COLOR_BGR2GRAY)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  diff = (np.substract(img,imgBW))/255
  
  if sum(sum(diff)) > 6200:
    return True
  else:
    return False
  
