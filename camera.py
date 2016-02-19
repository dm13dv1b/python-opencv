import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gray,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.CV_AA)
    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,nothing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
