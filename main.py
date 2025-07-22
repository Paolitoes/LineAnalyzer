import numpy as np
import cv2 as cv
import sys
import canny

img = cv.imread("line.png",cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

#dst = cv.addWeighted(img,0.7,img,0.3,0)
'''
The MyCanny implmentation uses a complex Scharr operator, and thus returns a complex 2dArray
aka, it does not return an array that can be shown as an image
using the np.angle function turns the complex array into a real one but it looks like either 
something is happening to the original img (not the file but the variable) or the angle are 
exploding and the grayscalling has a relative implementation and is exploding because of it
'''
grd = np.angle(canny.MyCanny(img))

dst = np.hstack((img,grd))

cv.imshow("Display window", dst)

k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("line.png",img)
