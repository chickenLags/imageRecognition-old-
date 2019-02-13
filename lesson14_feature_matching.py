import cv2
import numpy as np
import matplotlib.pyplot as plt

### FEATURE MATCHING
#
# it is similar to the template matching but allows for rotations
# and transformations too. it is done by bruteforcing, probably not
# very effective.

    # load images
img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)

    # orb??
orb = cv2.ORB_create()

    # get key points on both images
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

    # bf??
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    # find matches and sort them from highest to lowest (probability)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

    # create the image and add keypoints. looking at too many matches
    # will match to different objects. false positives. if an image has a
    # higher quality the amount of matches can be increased.
    # using a color image does not increase accuracy of findings. 
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

plt.imshow(img3)
plt.show()
