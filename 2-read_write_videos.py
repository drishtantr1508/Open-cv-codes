import cv2 as cv
import datetime
# cap = cv.VideoCapture('videos/VID_20201202_222857.mp4')
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,8000)#setting width parameter of the window
cap.set(cv.CAP_PROP_FRAME_HEIGHT,3000)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.mp4',fourcc,8,(1280,720))
print(cap.isOpened())

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        font = cv.FONT_HERSHEY_SIMPLEX
        text = f"Width : {str(cap.get(cv.CAP_PROP_FRAME_WIDTH))} Height : {str(cap.get(cv.CAP_PROP_FRAME_HEIGHT))} {str(datetime.datetime.now())}"
        frame = cv.putText(frame,text,(10,20),font,0.5,(0,0,0),1,cv.LINE_AA)#img, text, org, fontFace, fontScale, color[, thickness[, lineType
        cv.imshow('Drishtant the Great', frame)
        out.write(frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.imwrite('Clicked.jpg',frame)
            break
    else:
        break

cap.release()
cv.destroyAllWindows()