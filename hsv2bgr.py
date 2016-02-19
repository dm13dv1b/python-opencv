#!/usr/bin/python
import sys
import numpy as np
import cv2

print "HSV to RBG"
print 'Argument List:', str(sys.argv[1])

color_ = np.uint8([[[sys.argv[1],sys.argv[2],sys.argv[3]]]])
color_hsv = cv2.cvtColor(color_,cv2.COLOR_HSV2BGR)
print "BGR value:", color_hsv
