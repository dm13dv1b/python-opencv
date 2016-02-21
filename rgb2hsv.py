#!/usr/bin/python
import sys
import numpy as np
import cv2

print 'RGB to HSV'

print 'You must provide arguments in the following order: ./rgb2hsv.py 100 100 100'
print 'Where 100 100 100 stands for R G B'
print 'Argument list:', str(sys.argv[1])

color_ = np.uint8([[[sys.argv[3],sys.argv[2],sys.argv[1]]]])
color_hsv = cv2.cvtColor(color_,cv2.COLOR_BGR2HSV)
print "HSV value:", color_hsv
