import numpy as np
import cv2 as cv
import sys
import canny

img = cv.imread("line.png",cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")

#dst = cv.addWeighted(img,0.7,img,0.3,0)

grd = canny.MyCanny(img)

dst = np.hstack((img,grd))

cv.imshow("Display window", dst)

k = cv.waitKey(0)

if k ==ord("s"):
    cv.imwrite("line.png",img)
