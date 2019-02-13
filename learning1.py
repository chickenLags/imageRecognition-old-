# learning how to use openCV in this document.

import cv2
import numpy as np
import matplotlib.pyplot as plt

    # this imports an image and the argument makes it grayscale.
    # not specifying arg2 makes it read it as a colored image but
    # it removes the alpha channel. grayscale is prefered since its
    # simpler / easier. (less channels, less processing)
img = cv2.imread('roy.jpeg', cv2.IMREAD_GRAYSCALE)
#IMG_GRAYSCALE -> 0
#IMREAD_COLOR -> 1
#IMRED_UNCHANGED -> -1

'''
    # this code creates a window where arg0 is the window title and
    # arg1 is the image used. waitkey, waits for a key and destroy, closes it. 
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
    # shows the image with matplotlib. it also allows for drawing / plotting
    # on the image. imshow will be the prefered way though.
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80,100], 'c', linewidth=5)
plt.show()
'''

'''
    # this saves the image to the root directory 
cv2.imwrite('roygray.png', img)
'''

