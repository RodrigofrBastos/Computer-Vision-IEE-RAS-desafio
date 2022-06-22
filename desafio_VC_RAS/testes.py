import numpy as np
import cv2 as cv
import shutil
from skimage import io
import pytesseract
import os
import random

img = cv.imread('images/placaARG.jpeg')
cv.imshow("Color",img)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grey",grey)

canny = cv.Canny(img,125,175)
cv.imshow("Edge Cascaded image",canny)

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated images",dilated)

cv.waitKey(0)





'''
img = cv.cvtColor('images/penguin.jpeg', cv.COLOR_BGR2RGB)
img = cv.imread('images/penguin.jpeg',cv.COLOR_RGB2GRAY)

print(img.shape)

cv.imshow('img',img)
cv.waitKey(0)
cv.destoryAllWindows()
'''
