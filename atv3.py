import cv2
from random import randint

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
points = []
c=0
COLORS=[BLUE,GREEN,RED,BLACK,GRAY]


       
def click(event, x, y, flags, param):
  global point, pressed
  if event == cv2.EVENT_LBUTTONDOWN:
    points.append((x,y))
    
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")



if not capture.isOpened():
    print("Erro ao acessar o vídeo")
else:
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    newvideo = cv2.VideoWriter('newvideo.mp4',fourcc, 20.0, (640,480))
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            
            cv2.setMouseCallback("logo IF",click)
            for i in range(len(points)):
                cv2.circle(frame, points[i], 3,COLORS[c],-1)
            newvideo.write(frame)
            cv2.imshow('logo IF', frame)
          
            k=cv2.waitKey(20)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                
                break
            if cv2.waitKey(20) & 0xFF == ord('c'):
                c=randint(0,len(COLORS)-1)
            if k == 32:
                points.clear()
        else: break

capture.release()
newvideo.release()
cv2.destroyAllWindows()