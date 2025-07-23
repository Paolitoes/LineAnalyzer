import numpy as np
import cv2 as cv
import sys
import canny

img = cv.imread("Ghost1.png",cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

#dst = cv.addWeighted(img,0.7,img,0.3,0)

edges = cv.Canny(img,100,200)
ret, dots = cv.threshold(img,127,255,cv.THRESH_BINARY)

cv.imshow("Display window", img)
cv.imshow("Edges",edges)
cv.imshow("Dots",dots)

k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("edges.png",edges)
