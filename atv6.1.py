import cv2
BLUE = (255, 0, 0)
angulo= 0
pointc = (0,0)
rotacionado = 0

image = cv2.imread('ifma-caxias.jpg')

def click(event, x, y, flags, param):
  global pointc
  if event == cv2.EVENT_LBUTTONDOWN:
    pointc = (x,y)
    
cv2.namedWindow('atv6.1')
cv2.setMouseCallback("atv6.1",click)
cv2.imshow('atv6.1',image)

while(True): 
    
    rotacao = cv2.getRotationMatrix2D(pointc, angulo, 1.0)
    rotacionado = cv2.warpAffine(image, rotacao, (700, 517))
    cv2.circle(rotacionado, pointc, 3,BLUE,-1)
    cv2.imshow("atv6.1", rotacionado)
    
    k=cv2.waitKey(20)
    
    if k == ord('r'):
        angulo = angulo + 10
    if k == ord('l'):
        angulo = 0
        pointc = (0,0)
    if k == ord('q'):
        break
cv2.destroyAllWindows()