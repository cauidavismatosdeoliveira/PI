import cv2
import numpy as np

image = cv2.imread('logo-if.jpg')

def shineimg(img,b):
    shine = [b,b,b]
    res= np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            points = img[y,x]
            res[y, x] = np.maximum(np.minimum(points+shine,(255,255,255)),(0,0,0))
    return res

def contrastimg(img,contrast):
    res=np.zeros(img.shape, np.uint8)
   
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            points = img[y,x]
            res[y, x] = np.maximum(np.minimum(points*contrast,(255,255,255)),(0,0,0))
    return res

def negativeimg(img):
    res = np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            points = img[y,x]
            res[y, x] = np.maximum((255,255,255)- points,(0,0,0))
    return res

cv2.namedWindow('atv5')
shine = 0
contrast = 1
result = image
cv2.imshow('atv5',result)

while(True): 
    k=cv2.waitKey(20)
    
    if k == ord('a'):
        shine = min(shine+50,255)
        result = shineimg(image,shine)
        cv2.imshow('atv5',result)
        
    if k == ord('z'):
        shine = max(shine-50,-255)
        result = shineimg(image,shine)
        cv2.imshow('atv5',result)
        
    if k == ord('s'):
        contrast = min(contrast+0.25,2.0)
        result = contrastimg(image,contrast)
        cv2.imshow('atv5',result)
        
    if k == ord('x'):
        contrast = max(contrast-0.25,0.25)
        result = contrastimg(image,contrast)
        cv2.imshow('atv5',result)
        
    if k == ord('n'):
        result = negativeimg(result)
        cv2.imshow('atv5',result)
        
    if k == ord('q'):
        break

cv2.destroyAllWindows()
