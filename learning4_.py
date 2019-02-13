import numpy as np
import cv2

img = cv2.imread('roy.jpeg', cv2.IMREAD_COLOR)

    #referencing specific pixel which returns the color in array
    #this pixel can be changed as done below.
px = img[55, 55]
print(px)
img[55, 55] = [255, 255, 255]
print(px)

    #ROI = REGION OF AN IMAGE
    # this code allows for instant recoloring of an roi or to copy
    # and paste a roi. it is important that the areas are of the
    # same size. 
roi = img[100:150, 100:150]
#img[100:150, 100:150] = [255, 255, 255]
img[200:250, 100:150] = roi

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
