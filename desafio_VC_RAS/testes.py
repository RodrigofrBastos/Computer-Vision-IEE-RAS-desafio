from matplotlib.pyplot import imshow
import numpy as np
import cv2 as cv
import shutil
from skimage import io
import pytesseract
import os
import random


'''
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

'''




img = cv.imread('desafio_VC_RAS/images/A-placa-preta-pode-voltar-em-2021-para-carros-de-colecao.png')


imgResize = cv.resize(img, (962,623))

# grey = cv.cvtColor(imgResize,cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(grey,(7,7),cv.BORDER_DEFAULT)
# canny = cv.Canny(blur,125,175)
# dilated = cv.dilate(canny,(7,7),iterations=3)
# thresh = 255 - cv.threshold(dilated, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

extractedInformation = pytesseract.image_to_string(img)
print('placa: ',extractedInformation)

cv.imshow("thresh",img)


cv.waitKey(0)

'''
# Transforma em escala de cinza
gray = cv.cvtColor(imgResize, cv.COLOR_BGR2GRAY)
thresh = 255 - cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

# Aplica blur
thresh = cv.GaussianBlur(thresh, (3,3), 0)

# Realiza a extração de texto
placa = pytesseract.image_to_string(thresh)
print("placa é: ",placa)

cv.imshow("img",thresh)
cv.waitKey(0)
'''









