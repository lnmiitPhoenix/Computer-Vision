import cv2
import numpy as np

img = cv2.imread('mark.jpg')

#line
line=img.copy()
cv2.line(line,(310,179),(450,183),(255,0,0),thickness=5, lineType=cv2.LINE_AA)
cv2.imshow("line",line)

#rectangle
imageRectangle = img.copy()
cv2.rectangle(imageRectangle, (208, 55), (450, 355), (0, 255, 0), thickness=2, lineType=cv2.LINE_8)
cv2.imshow("rectangle", imageRectangle)
cv2.imwrite("imageRectangle.jpg", imageRectangle)

cv2.waitKey(0)
