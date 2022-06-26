import numpy as np
import cv2 as cv
import imutils as im
import pytesseract

'''
Equipe:
        Vagner Silva
        Rodrigo Bastos
        Rodrigo Sarno
'''

foto = '/desafio_VC_RAS/plate-images/placa1.jpeg'
trocar = '123456'
lista = []

for i in range(len(trocar)):

    imagem = cv.imread(foto.replace(foto[27], trocar[i]))
    cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    cinza = cv.bilateralFilter(cinza, 13, 15, 15)
    borda = cv.Canny(cinza, 30, 200)

    contornos=cv.findContours(borda.copy(),cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contornos = im.grab_contours(contornos)
    contornos = sorted(contornos,key=cv.contourArea, reverse = True)[:10]
    contornoImagem = None

    for j in contornos:
        perimetro = cv.arcLength(j, True)
        aproxima = cv.approxPolyDP(j, 0.018 * perimetro, True)
        if len(aproxima) == 4:
            contornoImagem = aproxima
            break

    mascara = np.zeros(cinza.shape,np.uint8)
    novaImagem = cv.drawContours(mascara,[contornoImagem],0,255,-1,)
    novaImagem = cv.bitwise_and(imagem,imagem,mask=mascara)

    (x, y) = np.where(mascara == 255)
    (topox, topoy) = (np.min(x), np.min(y))
    (inferiorx, inferiory) = (np.max(x), np.max(y))
    cortado = cinza[topox:inferiorx+1, topoy:inferiory+1]

    texto = pytesseract.image_to_string(cortado, config='--psm 11')
    print(f'\nO número da placa é: {texto.upper()}')
    lista.append(texto)
print(lista)