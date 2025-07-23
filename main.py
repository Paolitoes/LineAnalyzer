import numpy as np
import cv2 as cv
import sys
import canny

img = cv.imread("Ghost1.png",cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

#dst = cv.addWeighted(img,0.7,img,0.3,0)

lines = canny.MyCanny(img)
oficline = cv.Canny(img,100,200)

cv.imshow("Display window", lines)
cv.imshow("Second window", img)
cv.imshow("Third window",oficline)

k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("lines.png",oficline)
