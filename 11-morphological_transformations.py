import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('photos/color_balls.jpg', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

# It increses the size of image by a slight at thr borders...
dilation = cv2.dilate(mask, kernal, iterations=2)

# It decreases the size by a slight at the border.
erosion = cv2.erode(mask, kernal, iterations=1)

# Erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Dilation followed by erosion.
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# Difference between dilation and erosion of an image.
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# Difference between opening and input image.
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

# Difference between closing and input image.
bh = cv2.morphologyEx(mask,  cv2.MORPH_BLACKHAT, kernal)

titles = ['image', 'mask', 'dilation',
          'erosion', 'opening', 'closing', 'Morph Gradient', 'Top Hat', 'Black Hat']
images = [img, mask, dilation, erosion, opening, closing, mg, th, bh]

for i in range(len(titles)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
