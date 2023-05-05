import numpy as np
import cv2

img = cv2.imread('ifma-logo.png')
mask = cv2.imread('Mask.png',0)
cv2.imshow("imagem original",img)
rows,cols = mask.shape
roi = img[0:rows, 0:cols]

telea = cv2.inpaint(roi,mask,3,cv2.INPAINT_TELEA)
img[0:rows, 0:cols] = telea
cv2.imshow("telea",img)

ns = cv2.inpaint(roi,mask,3,cv2.INPAINT_NS)
img[0:rows, 0:cols] = ns
cv2.imshow("ns",img)

cv2.waitKey(0)
cv2.destroyAllWindows()