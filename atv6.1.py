import cv2
BLUE = (255, 0, 0)
angle= 0
pointc = (0,0)
rotated = 0
width = 0
height = 0

image = cv2.imread('ifma-caxias.jpg')
height, width = image.shape[:2]
def click(event, x, y, flags, param):
  global pointc
  if event == cv2.EVENT_LBUTTONDOWN:
    pointc = (x,y)
    
cv2.namedWindow('atv6.1')
cv2.setMouseCallback("atv6.1",click)
cv2.imshow('atv6.1',image)

while(True): 
    
    rotation = cv2.getRotationMatrix2D(pointc, angle, 1.0)
    rotated = cv2.warpAffine(image, rotation, (width, height))
    cv2.circle(rotated, pointc, 3,BLUE,-1)
    cv2.imshow("atv6.1", rotated)
    
    if angle > 360: angle = 0
    
    k=cv2.waitKey(20)
    
    if k == ord('r'):
        angle = angle + 10
    if k == ord('l'):
        angle = 0
        pointc = (0,0)
    if k == ord('q'):
        break
cv2.destroyAllWindows()