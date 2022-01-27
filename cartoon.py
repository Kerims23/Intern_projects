#importing the libraries 
import cv2
import numpy as np

#read the image 
img = cv2.imread("img.png")

#edges 
gray = cv2.cvt Color (img, cv2.COLOR_BGR2GRAY)
gray = cv2.median_blur (gray, 5)

