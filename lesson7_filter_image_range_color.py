import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
        # hsv is a way to define colors. this makes it easier to work on the
        # intensity of the color.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # defines the lower and upper colors that will be used by the mask
    lower_red = np.array([0,100,100])
    upper_red = np.array([80, 255, 255])
        # a mask that gives true if its between a certain range and false if not
    mask = cv2.inRange(hsv, lower_red, upper_red)
        # shows the image if the mask is true
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    
    

    cv2.imshow('original', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
