# morphological transformations

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

    ### lesson 9  starts here
    #
    # there are multiple types, erosion and dialation are being used first.
    # erosion slides through the image and if they are all the same then it
    # continues on, however if there is a pixel thats different then it will
    # remove that pixel.
    # dialation, does the opposite by pushing out...?

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    # there are four more that are available, opening and closing:
    # opening removes false positives
    # closing removes false negatives
    #   meybe i can use them in conjunction
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # tophat: the difference between input image and opening of the image
    # blackhat: the difference between the clsoing and the input image
    # not implemented here... pls stop failing sentdex...

    cv2.imshow('original', frame)
    cv2.imshow('res', res)

    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
