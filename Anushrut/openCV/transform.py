
import cv2
import numpy as np

# Read image
source = cv2.imread("sample.jpg",1);

# Createmask/ warp matrix
warpMat = np.float32([[1.2, 0.2, 2],[-0.3, 1.3, 1]])

# Another mask/warp matrix
warpMat2 = np.float32([[1.2, 0.3, 2],[0.2, 1.3, 1]])

# Use warp affine
result = cv2.warpAffine(source, warpMat,(int(1.5*source.shape[0]),
         int(1.4*source.shape[1])), None, flags=cv2.INTER_LINEAR,
         borderMode=cv2.BORDER_REFLECT_101 )

result2 = cv2.warpAffine(source, warpMat2, (int(1.5*source.shape[0]),
          int(1.4*source.shape[1])), None, flags=cv2.INTER_LINEAR)#,          borderMode=cv2.BORDER_REFLECT_101)

# Display images
cv2.imshow("Original",source)
cv2.imshow("Result", result)
cv2.imshow("Result2", result2)
cv2.waitKey(0)




im_src = cv2.imread('book2.jpg')
# Four corners of the book in source image
pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])


# Read destination image.
im_dst = cv2.imread('book1.jpg')
# Four corners of the book in destination image.
pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])

# Calculate Homography
h, status = cv2.findHomography(pts_dst, pts_src)

# Warp source image to destination based on homography
im_out = cv2.warpPerspective(im_dst, h, (im_src.shape[1],im_src.shape[0]))

# Display images
cv2.imshow("Source Image", im_src)
cv2.imshow("Destination Image", im_dst)
cv2.imshow("Warped Source Image", im_out)

cv2.waitKey(0)
