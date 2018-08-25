import cv2

import numpy as np
cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
while(1):
    # Take each frame
    ret, frame = cap.read()
    # convert img to gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # blurred image to improve smoothness
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edge1=cv2.Canny(gray,100,200,)
    edge2=cv2.Canny(gray,50,200,)
    edge3=cv2.Canny(gray,100,50,)

    cv2.imshow("frame",frame)

    ## additional frame overriding to observe changes in the original img
    # res = cv2.bitwise_and(frame,frame,mask=edge3)
    # cv2.imshow("over",res)

    cv2.imshow("edge-3",edge1)
    cv2.imshow("edge-10",edge2)
    cv2.imshow("edge-25",edge3)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
