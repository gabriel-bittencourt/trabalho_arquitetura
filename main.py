import cv2
import color_detect
import os
import glob

file_list = glob.iglob("faces/*.jpg")

for file in file_list:
    #Para cada arquivo na lista faça:
    #Estabelece os classificadores de face

    # face_cascade = cv2.CascadeClassifier('/home/gabriel/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml')
    # face_alt_cascade = cv2.CascadeClassifier('/home/gabriel/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_alt.xml')
    # face_alt2_cascade = cv2.CascadeClassifier('/home/gabriel/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_alt2.xml')
    # face_alt_tree_cascade = cv2.CascadeClassifier('/home/gabriel/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_alt_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    face_alt2_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    face_alt_tree_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt_tree.xml")

    #Lê a imagem e converte para escala de cinza
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Faz as classificações
    face = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    # faces2 = face_alt_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    # faces3 = face_alt2_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
    # faces4 = face_alt_tree_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))

    print("Arquivo:", file)
    altura, largura, channels = img.shape
    print("w: %d; h: %d" %(altura, largura))

    for (x,y,w,h) in face:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]


        # Aqui acha a cor das roupas

        # Posicao roupa cima
        yc = (y+h) + (h)
        hc = h // 2
        
        # Posicao roupa baixo
        yb = (y+h) + 4*h + (h // 8)
        hb = h // 2

        # Cor roupa cima
        if(yc < altura):
            print("Roupa de cima: ", end = "")
            color_detect.detect(file, x, yc, w, hc)
            
            # cv2.rectangle(img,(x,yc),(x+w,yc+hc),(255,0,0),2)
            # roi_gray = gray[y:y+h, x:x+w]
        else:
            print("y:", y)

        # Cor roupa baixo
        if(yb < altura):
            print("Roupa de baixo: ", end = "")

            color_detect.detect(file, x, yb, w, hb)
            
            #cv2.rectangle(img,(x, yb), (x+w, yb+hb), (255,0,0),2)
            #roi_gray = gray[y:y+h, x:x+w]
        else:
            print("y:", y)

        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # roi_gray = gray[y:y+h, x:x+w]

        # roi_color = img[y:y+h, x:x+w]

        cv2.imshow("img", img)
        cv2.waitKey(0)

        print()

    #Exibe as imagens com retãngulos.
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

