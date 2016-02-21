import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((200,512,3), np.uint8)
cv2.namedWindow('Color settings')

# Create trackbars for color change
cv2.createTrackbar('low R','Color settings',40,255,nothing)
cv2.createTrackbar('low G','Color settings',43,255,nothing)
cv2.createTrackbar('low B','Color settings',50,255,nothing)
cv2.createTrackbar('high R','Color settings',100,255,nothing)
cv2.createTrackbar('high G','Color settings',100,255,nothing)
cv2.createTrackbar('high B','Color settings',100,255,nothing)

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get current positions of four trackbars
    low_r = cv2.getTrackbarPos('low R','Color settings')
    low_g = cv2.getTrackbarPos('low G','Color settings')
    low_b = cv2.getTrackbarPos('low B','Color settings')
    
    # Convert RGB trackbars to HSV
    #hsv_array = np.uint8([[[b,g,r]]])
    hsv_array = np.array([[[low_b, low_g, low_r]]], np.uint8)
    hsv_converted = cv2.cvtColor(hsv_array,cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    r = hsv_converted[0,0,0]
    g = hsv_converted[0,0,1]
    b = hsv_converted[0,0,2]
    lower_blue = np.array([r,g,50])
    upper_blue = np.array([130,255,255])
    print str(hsv_converted[0,0,0])+" "+str(hsv_converted[0,0,1])+" "+str(hsv_converted[0,0,2])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #img[:] = [low_b,low_g,low_r]
    img[:] = [0, 0, 0]    
    # Print values to live image
    text_color = (255,0,0)
    cv2.putText(img, ("Lower colors"), (10,20), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("RED: " + str(low_r)), (10,40), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("GREEN: " + str(low_g)), (10,60), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("BLUE: " + str(low_b)), (10,80), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("HSV: " + str(hsv_converted)), (10,100), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    cv2.putText(img, ("lower_blue: " + str(lower_blue)), (10,120), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)
    # Update windows
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('Color settings',img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
