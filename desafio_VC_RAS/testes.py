from matplotlib.pyplot import imshow
import numpy as np
import cv2 as cv
import shutil
from skimage import io
import pytesseract
import os
import random


#           TIPOS DE FILTROS PARA AS IMAGENS

# img = cv.imread('desafio_VC_RAS/images/placaARG.jpeg')
# imgResize = cv.resize(img, (962,623))
# cv.imshow("Color",imgResize)

# grey = cv.cvtColor(imgResize,cv.COLOR_BGR2GRAY)
# cv.imshow("grey",grey)

# blur = cv.GaussianBlur(imgResize,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("Blurred",blur)

# canny = cv.Canny(imgResize,125,175)
# cv.imshow("Edge Cascaded image",canny)

# dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow("dilated images",dilated)

# imgHSV = cv.cvtColor(imgResize, cv.COLOR_BGR2HSV)
# cv.imshow("imgHSV", imgHSV)

kernel = np.ones((2,2),np.uint8)

img = cv.imread('desafio_VC_RAS/images/placaARG.jpeg')
imgResize = cv.resize(img, (962,623))

imgHSV = cv.cvtColor(imgResize, cv.COLOR_BGR2HSV)
grey = cv.cvtColor(imgHSV,cv.COLOR_BGR2GRAY)


h_min = 0
h_max = 360
s_min = 0
s_max = 255
v_min = 0
v_max = 50

lower = np.array([h_min,s_min,v_min])
upper = np.array([h_max,s_max,v_max])

# Criação de máscara com base nos limites estabelecidos
mask = cv.inRange(imgHSV,lower,upper)
canny = cv.Canny(mask,125,175)
blur = cv.GaussianBlur(canny,(7,7),cv.BORDER_DEFAULT)
imgEroded = cv.erode(blur,kernel,iterations=1)
thresh = 255 - cv.threshold(imgEroded, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

extractedInformation = pytesseract.image_to_string(thresh)
print('placa: ',extractedInformation)

cv.imshow("thresh",thresh)

cv.waitKey(0)