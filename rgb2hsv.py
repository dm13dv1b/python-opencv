#!/usr/bin/python
import sys
import numpy as np
import cv2

print "RGB to HSV"
print 'Argument List:', str(sys.argv[1])

color_ = np.uint8([[[sys.argv[3],sys.argv[2],sys.argv[1]]]])
color_hsv = cv2.cvtColor(color_,cv2.COLOR_BGR2HSV)
print "HSV value:", color_hsv
