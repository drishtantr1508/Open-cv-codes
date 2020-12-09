import numpy as np

import cv2

img = cv2.imread ('photos/kali.jpg')

img2 = cv2.imread ("photos/book.jpg")

print (img.shape) # returns a tuple of number of rows, co 
print (img.size) # returns Total number of pixels is acces 
print (img.dtype) # returns Image datatype is obtained 
b,g,r = cv2.split (img) 

img = cv2.merge((b, g, r))

ball = img [280:340, 330:390]
img [273:333, 100:160] = ball

img = cv2.resize (img, (1800, 900))
img2 = cv2.resize (img2, (1800, 900))

dst = cv2.addWeighted  (img, .7, img2, .3, 0); 

cv2.imshow ('image', dst)

#dst = cv2.add (img, img2) |

k = cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("mouseclick2.png",img)
    cv2.destroyAllWindows()



#######################################################

#######################################################


# import cv2
# import numpy as np
# img = cv2.imread('189book.png')


# books = img[102:820,748:1600]
# img[0:718,0:852] = books
# # cv2.imshow('Books',books)
# cv2.imshow('Image',img)
# k = cv2.waitKey()
# if k==27:
#     cv2.destroyAllWindows()
# elif k==ord('s'):
#     cv2.imwrite("mouseclick2.png", img)
#     cv2.destroyAllWindows()