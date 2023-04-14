import cv2
import numpy as np

img = cv2.imread('noise.jpg')

median = cv2.medianBlur(img,7)
#blur = cv2.blur(img,(7,7))
#glaussian = cv2.GaussianBlur(img,(7,7),0)

while(True):
    
    cv2.imshow('Original.jpg',img)
    
    cv2.imshow('Mediana.jpg',median)
    
    #cv2.imshow('glausian.jpg',glaussian)
    
    #cv2.imshow('blur.jpg',blur)
    
    k=cv2.waitKey(20)
    
    if k == ord('q'):
        break

cv2.destroyAllWindows()