from matplotlib.pyplot import imshow
import numpy as np
import cv2 as cv
import shutil
from skimage import io
import pytesseract
import os
import random

img = cv.imread('desafio_VC_RAS/images/placaARG.jpeg')
imgResize = cv.resize(img, (962,623))
cv.imshow("Color",imgResize)

grey = cv.cvtColor(imgResize,cv.COLOR_BGR2GRAY)
cv.imshow("grey",grey)

blur = cv.GaussianBlur(imgResize,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blurred",blur)

canny = cv.Canny(imgResize,125,175)
cv.imshow("Edge Cascaded image",canny)

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated images",dilated)

imgHSV = cv.cvtColor(imgResize, cv.COLOR_BGR2HSV)
cv.imshow("imgHSV", imgHSV)

cv.waitKey(0)

