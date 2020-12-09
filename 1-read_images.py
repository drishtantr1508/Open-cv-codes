import cv2 as cv
import numpy as np

book_img = cv.imread('photos/small_book.jpg', 1)
# book_img = np.zeros([512,512,3],np.uint8)
book_img = cv.rectangle(book_img, (0, 0), (255, 255), (0, 255, 0), -1)
book_img = cv.line(book_img, (0, 0), (255, 255), (255, 0, 0), 10)
book_img = cv.arrowedLine(book_img, (0, 255), (255, 255), (255, 255, 0), 10)
book_img = cv.circle(book_img, (255, 255), 50, (231, 123, 134), -1)
font = cv.FONT_HERSHEY_SIMPLEX
book_img = cv.putText(book_img, 'Drishtant Rai',
                      (3, 125), font, 2.5, (255, 0, 255))
cv.imshow('Book', book_img)
print(book_img)

k = cv.waitKey()
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("photos/small_book_copy.png", book_img)
    cv.destroyAllWindows()
