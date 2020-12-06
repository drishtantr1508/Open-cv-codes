# ########################################
# # EXAMPLE 1
# ########################################

# import numpy as np
# import cv2 as cv

# def nothing(x):
#     print(x)

# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv.namedWindow('image')

# cv.createTrackbar('B', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0, 255, nothing)
# cv.createTrackbar('R', 'image', 0, 255, nothing)

# switch = '0 : OFF\n 1 : ON'
# cv.createTrackbar(switch, 'image', 0, 1, nothing)

# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break

#     b = cv.getTrackbarPos('B', 'image')
#     g = cv.getTrackbarPos('G', 'image')
#     r = cv.getTrackbarPos('R', 'image')
#     s = cv.getTrackbarPos(switch, 'image')

#     if s == 0:
#        img[:] = 0
#     else:
#        img[:] = [b, g, r]


# cv.destroyAllWindows()

########################################
# EXAMPLE 2
########################################

import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

# Create a black image, a window
cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('photos/small_book.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       pass
    else:
       img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image',img)

cv.destroyAllWindows()