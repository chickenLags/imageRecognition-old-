#drawing on images with opencv. this is more efficient than matplotlib
import numpy as np
import cv2

img = cv2.imread('roy.jpeg', cv2.IMREAD_COLOR)
    #this code simply draws LINE like in learning1 with plt. 
    # the args in this function are:
    # img, start line, end line, color BGR, line width
cv2.line(img, (0,0), (150, 150), (255, 255, 255), 15)
    #this does the same thing but as a RECTANGLE instead of line
    # arguments are:
    # img, topleft corner, bottom right corner, color, width
cv2.rectangle(img, (15, 25), (200, 150), (0,255,0), 5)
    # draws a CIRCLE with the arguemns:
    # img, center, radius, color and line width or -1 for filled
cv2.circle(img, (100, 63), 55, (0,0,255), -1)
    # make a POLYGON by using a np array, arguments are:
    # img, pnt_array, connected, color, linewidth
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,  1, 2)) #reshapes datatype
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

    # this writes TEXT to the image, by making a font and then use it with
    # the keyword, which ahs the arguments
    # img, text, position, font, size, color, thickness, anti aliasing
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

    #

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
