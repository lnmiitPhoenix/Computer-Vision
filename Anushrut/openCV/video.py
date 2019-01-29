import cv2
import numpy as np

cap=cv2.VideoCapture("chaplin.mp4") #for live camera setup pass 0 ,1,2 .. instead of video name

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:

        cv2.imshow('frame',frame)

        if cv2.waitKey(16) & 0xFF ==27:
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)

# get sysem dependent frame size

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc('M','J','P','G'),25,(frame_width,frame_height))

while(True):
    ret,frame=cap.read()

    if ret==True:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF ==27:
            break
    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()
