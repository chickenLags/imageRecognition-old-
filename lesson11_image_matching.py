import cv2
import numpy as np

# in this lesson a template will be looked for in a different image
# in this case we look for a power port on a stack of raspberries
# template matching is very precise and should be used for things that
# are always the same.

img = cv2.imread('raspberry_img.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.imread('template.jpg', 0) # <-- MAKE SURE TO ADD THE 0
#temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
w, h = temp.shape[::-1]


res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
