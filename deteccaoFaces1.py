#import libraries
import cv2
import numpy as np

# Importando Classificador para deteccaoo de face
classificadorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def detectorFace (img, size=0.5):
    
    # COnvertendo imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imGray = cv2.imshow('imagem cinza', gray)
    #v2.waitKey(0)
    faces = classificadorFace.detectMultiScale(gray, 1.3, 5)
    #print(type(faces))
    #print('FACES:')
    #print(faces)

    if faces == ():
        print('Nao foi detectada nenhuma face na imagem.')
    else:
        n = len(faces)
        print(n)
        imgFace = img.copy()
        facesLista = faces.tolist()

        for j in range(n):
            x = facesLista[j][0]
            y = facesLista[j][1]
            w = facesLista[j][2]
            h = facesLista[j][3]
            print(x,y,w,h)
            imFace = cv2.rectangle (imgFace, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #cv2.imshow("Crianca j", imFace)
            #cv2.waitKey
        return imFace, n

# Importando imagem a ser detectada a face
imCaminho = input("Coloque o caminho para imagem a ser detectada a face:\n")
im = cv2.imread(imCaminho)
cv2.imshow('input image', im)
cv2.waitKey(0)

#chamando funcao de deteccao
rois_face, qtdFaces = detectorFace (im)
if rois_face != ():
    #Mostrando a ROI
    cv2.imshow("Faces destacadas",rois_face)
    cv2.waitKey(0)
    print('O numero de faces detectadas foram:')
    print(qtdFaces)





