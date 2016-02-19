import cv2
import numpy as np

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_SIMPLEX

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    print r,g,b
    hsv = np.uint8([[[b,g,r]]])
    hsv_converted = cv2.cvtColor(hsv,cv2.COLOR_BGR2HSV)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    text_color = (255,0,0)
    cv2.putText(img, ("RED: " + str(r)), (10,20), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("GREEN: " + str(g)), (10,40), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("BLUE: " + str(b)), (10,60), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("HSV: " + str(hsv_converted)), (10,80), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.imshow('image',img)

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
