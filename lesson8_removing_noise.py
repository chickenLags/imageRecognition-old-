import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
        # hsv is a way to define colors. this makes it easier to work on the
        # intensity of the color.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # defines the lower and upper colors that will be used by the mask
    lower_red = np.array([0,150,100])
    upper_red = np.array([80, 255, 255])
        # a mask that gives true if its between a certain range and false if not
    mask = cv2.inRange(hsv, lower_red, upper_red)
        # shows the image if the mask is true
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    ### from this point onward is lesson 8

        # a kernal will be made to remove noise
        # as sonny talked about before this is a grid that will be moved over
        # the image to check whether its true. it removes a lot of clarity. 
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)

        # gaussian blur is an alternative
    blur = cv2.GaussianBlur(res, (15, 15), 0)

        # median blur is also another alt
    median = cv2.medianBlur(res, 15)
        # bilateral blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    
    

    cv2.imshow('original', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    #cv2.imshow('smooth', smoothed)
    #cv2.imshow('gaus', blur)
    cv2.imshow('median', median)
    #cv2.imshow('bilateral', bilateral)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
