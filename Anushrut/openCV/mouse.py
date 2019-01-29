import cv2
import numpy as np
import math


center=[]
circum=[]
ix=-1
iy=-1

def drawcir(action,x,y,flag,data):
    
    global center, circum, ix, iy

    if action==cv2.EVENT_LBUTTONDOWN:
        ix=x
        iy=y
        cv2.rectangle(source,(0,0),(1,1),(255,0,0),-1)
    elif action == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(source,(ix,iy),(x,y),(255,0,0),-1)


    if action==cv2.EVENT_RBUTTONDOWN:
        center=[(x,y)]
        #mark center
        cv2.circle(source, center[0], 1, (255,255,0), 2, cv2.LINE_AA )

    elif action==cv2.EVENT_RBUTTONUP:
        circum=[(x,y)]

        radius = math.sqrt(math.pow(center[0][0]-circum[0][0],2)
                    +math.pow(center[0][1]-circum[0][1],2))
        # Draw the circle
        cv2.circle(source, center[0], int(radius), (0,255,0),2, cv2.LINE_AA)
        # cv2.imshow("Window",source)


source=cv2.imread('sample.jpg')

copy=source.copy()

cv2.namedWindow("Window")

cv2.setMouseCallback("Window",drawcir)# call function with mouse action

k=0
#loop till escape
while k!=27:

    cv2.imshow("Window",source)
    cv2.putText(source,"Choose center, and drag, Press ESC to exit and c to clear" ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    # if k==99:
    #     source = copy.copy()

cv2.destroyAllWindows()
