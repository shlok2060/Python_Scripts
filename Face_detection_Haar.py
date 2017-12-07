#importing required libraries
import cv2
import math
import sys
import matplotlib.pyplot as plt
path_of_haar="/home/brainsick/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
path_of_image="/home/brainsick/Code/img.jpg"
#the path of the haar cascade classifier we intend to use in this detection
def converttoRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Loading the test image as a Numpy array
img=cv2.imread(path_of_image)
try:
    plt.imshow(img)
except TypeError:
    print("Error! File does not exist")
    sys.exit()
#As Haar cascades expect gray image to detect Haar like features we will convert them to grayscale
def converttogray(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gimg=converttogray(img)
#As Linux does not support cv2.imshow so using it plt.imshow cause support
#plt.imshow(gimg,cmap="gray")
def facedetect(gimg):
    gimg=converttogray(img)
    haar_classifier=cv2.CascadeClassifier(path_of_haar)
    faces=haar_classifier.detectMultiScale(gimg,scaleFactor=1.2,minNeighbors=5)
    return faces
def printfacecount(gimg):
    print(len(facedetect(gimg)),"Faces in this picture")
def selectfaces(gimg):
    faces=facedetect(gimg)
    s=img.copy()
    for (x,y,w,h) in faces:
        a=math.sqrt(w**2+h**2)
        cv2.rectangle(s,(x,y),(x+w,y+h),(0,0,255),2)
    printfacecount(gimg)
    plt.imshow(converttoRGB(s))
    plt.show()
selectfaces(img)
