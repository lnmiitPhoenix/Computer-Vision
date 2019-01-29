import numpy as np
import cv2
#stored in a numpy array img
img= cv2.imread('sample.jpg')

img2=img.copy()

imgRo=img.shape[0]
imgCo=img.shape[1]
ro=imgRo/2
co=imgCo/2
ro=int(ro)
co=int(co)


crop=img[0:ro,co:imgCo]


re=cv2.resize(img,(230,150),interpolation=cv2.INTER_CUBIC)


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dim=img.shape
rAngle= +45
scale=2

rMat=cv2.getRotationMatrix2D((dim[0]/2,dim[1]/2),rAngle,1)#center,angle,scale
# always warp rotated
rotate=cv2.warpAffine(img,rMat,(dim[1],dim[0]))
cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("crop",crop)
cv2.imshow("resize",re)
cv2.imshow("rotate",rotate)

cv2.waitKey(0)
