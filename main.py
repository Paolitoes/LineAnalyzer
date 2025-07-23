import numpy as np
import cv2 as cv
import sys
import canny

img = cv.imread("Ghost1.png",cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

thresh = lambda x: cv.threshold(x,115,255,cv.THRESH_BINARY)

def dotdetect(img1):
    temp = cv.GaussianBlur(img1,(7,7),0)
    ret2, temp = thresh(temp)
    return temp


edges = cv.Canny(img,100,200)
dots = dotdetect(img)
ret, thrImg = thresh(img)
erosion = cv.erode(255-thrImg,np.ones((5,5),np.int8))

cv.rectangle(img,(0,0),(7,7),0)

cv.imshow("Display window", img)
cv.imshow("Edges",edges)
cv.imshow("Dots",dots)
cv.imshow("Erosion",erosion)

k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("edges.png",edges)
