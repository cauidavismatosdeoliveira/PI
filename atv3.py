import cv2
from random import randint

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
point = (0,0)
c=0
COLORS=[BLUE,GREEN,RED,BLACK,GRAY]

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c=randint(0,len(COLORS)-1)
        cv2.circle(frame,(x,y),3,COLORS[c],-1)
       
def click(event, x, y, flags, param):
  global point, pressed
  if event == cv2.EVENT_LBUTTONDOWN:
    point = (x,y)
    
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")



if not capture.isOpened():
    print("Erro ao acessar o vídeo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            video =  frame
            cv2.setMouseCallback("logo IF",click)
            
            cv2.circle(frame, point, 3,COLORS[c],-1)
            cv2.imshow('logo IF', video)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                cv2.imwrite('newvideo.mp4',video)
                break
            if cv2.waitKey(20) & 0xFF == ord('c'):
                c=randint(0,len(COLORS)-1)
               
        else: break

capture.release()
cv2.destroyAllWindows()