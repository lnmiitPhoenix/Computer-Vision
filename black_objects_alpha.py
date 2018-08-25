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
    #lower_blue = np.array([100,100,100])
    #upper_blue = np.array([140,255,255])

    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,30])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
   # mask2 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
   # mask3 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= dilation)
    cv2.imshow('frame',frame)
##    cv2.imshow('mask',mask)
##    cv2.imshow('dialted',dilation)
##    cv2.imshow('res',res)
    img=np.uint8([[[0,0,0]]])
    (_,contours,hierarchy)=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    cv2.imshow("Color Tracking",img)
    output = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 20)

# ensure at least some circles were found
    if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
          # draw the circle in the output image, then draw a rectangle
          # corresponding to the center of the circle
          cv2.circle(output, (x, y), r, (0, 255, 0), 4)

          cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	# show the output image
        cv2.imshow("output", output)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
