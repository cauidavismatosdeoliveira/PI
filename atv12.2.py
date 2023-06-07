import cv2
import numpy as np

img = cv2.imread('coins.jpeg')

img_blur = cv2.medianBlur(img, 5)
img_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,
                           1, 100, param1=150, param2=50)


circles=np.uint(circles[0])
print(circles)

COLOR1 = (255, 0, 0)
COLOR2 = (0, 0, 255)
COINS = {73:'50cents', 64:'5cents', 85:'1real', 59:'10cents', 72:'25cents'} #dicionario

for i in circles:
    x, y, r = i

    cv2.circle(img, (x, y), r, COLOR1, 2) #circulo externo
    x1 = int(x-25)
    text = COINS[r] #texto
    cv2.putText(img, text, (x1, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, COLOR2, 2, cv2.LINE_AA) #texto

cv2.imshow('Coins', img)

cv2.waitKey(0)
cv2.destroyAllWindows()