#importing the libraries 
import cv2
import numpy as np

#read the image 
img = cv2.imread("img.png")

#edges 
gray = cv2.cvt Color (img, cv2.COLOR_BGR2GRAY)
gray = cv2.median_blur (gray, 5)
edges = cv2.adaptive Threshold (gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
