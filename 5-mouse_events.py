import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()