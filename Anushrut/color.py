import cv2

import numpy as np
cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,100,100])
    upper_blue = np.array([140,255,255])

    lower_red = np.array([0,200,100])
    upper_red = np.array([10,255,255])

    lower_green = np.array([50,80,100])
    upper_green = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    b1 = cv2.inRange(hsv, lower_blue, upper_blue)
    # using dilation and morph open to improve recognition
    b2 = cv2.dilate(b1,kernel,iterations = 1)
    b3 = cv2.morphologyEx(b2, cv2.MORPH_OPEN, kernel)


    r1 = cv2.inRange(hsv, lower_red, upper_red)
    # using dilation and morph open to improve recognition
    r2 = cv2.dilate(r1,kernel,iterations = 1)
    r3 = cv2.morphologyEx(r2, cv2.MORPH_OPEN, kernel)


    g1 = cv2.inRange(hsv, lower_green, upper_green)
    # using dilation and morph open to improve recognition
    g2 = cv2.dilate(g1,kernel,iterations = 1)
    g3 = cv2.morphologyEx(g2, cv2.MORPH_OPEN, kernel)

    # morph close didn't improve
   # mask3 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
    # Bitwise-AND mask and original image
    red = cv2.bitwise_and(frame,frame, mask= r3)
    blue = cv2.bitwise_and(frame,frame, mask= b3)
    green = cv2.bitwise_and(frame,frame, mask= g3)
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',g2)
    cv2.imshow('green',green)
    cv2.imshow('blue',blue)
    cv2.imshow('red',red)
    img=np.uint8([[[0,0,0]]])
    (contours,hierarchy)=cv2.findContours(b3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))


    (contours,hierarchy)=cv2.findContours(g3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"green color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))


    (contours,hierarchy)=cv2.findContours(r3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"red color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    cv2.imshow("Color Tracking",img)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
