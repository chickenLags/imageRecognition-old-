import cv2
import numpy as np


### BACKGROUND REDUCTIONS / REMOVAL, FOREGROUND EXTRACTION
#
# it finds changes compared to the previous frame and then
# marks it as foreground.

#cap = cv2.VideoCapture('people-walking.mp4')
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    fgmask = fgbg.apply(frame)

        # i should remove background noise...
    kernel = np.ones((5,5), np.uint8)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        # maybe i can have expand the mask to fit the whole object istead
        # only some part
    erosion = cv2.erode(fgmask, kernel, iterations = 1)
    dilation = cv2.dilate(closing, kernel, iterations = 5)
    
        # show only the moving parts:
    res = cv2.bitwise_and(frame, frame, mask = dilation)
    res_vanilla = cv2.bitwise_and(frame, frame, mask = erosion)
    

    cv2.imshow('original', frame)
    cv2.imshow('fg', opening)
    cv2.imshow('result', res)
    cv2.imshow('vanilla', res_vanilla)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
