import numpy as np
import cv2 as cv
import sys
import canny

ImagePath = "Ghost1.png"

imgC = cv.imread(ImagePath)
imgG = cv.imread(ImagePath,cv.IMREAD_GRAYSCALE)

if imgC is None or imgG is None:
    sys.exit("Could not read the image.")

def thresh(x):
    _, thr = cv.threshold(x,100,255,cv.THRESH_BINARY)
    return thr

dots = thresh(imgG)

r,c=np.nonzero(dots>0)
print(r)
print(r.size)
print(c)
print(c.size)

for p in zip(r,c):
    cv.circle(imgC,p,5,(255,0,0))

cv.imshow("Overlay Window",imgC)
cv.imshow("gray",imgG)
cv.imshow("thr",dots)
#imgC is showing up as 3/4th blue, I'm blaming the circle drawing

'''
def dotdetect(img1):
    temp = cv.GaussianBlur(img1,(7,7),0)
    ret2, temp = thresh(temp)
    return temp


edges = cv.Canny(img,100,200)
dots = dotdetect(img)
ret, thrImg = thresh(img)
erosion = cv.erode(255-thrImg,np.ones((4,4),np.int8))

cv.rectangle(img,(0,0),(7,7),0)

cv.imshow("Display window", img)
cv.imshow("Edges",edges)
cv.imshow("Dots",dots)
cv.imshow("Erosion",erosion)
'''
k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("edges.png",edges)
