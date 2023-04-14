import cv2


capture = cv2.VideoCapture("IFMA.mp4")
img2 = cv2.imread('logo-if.jpg')

img2 = cv2.resize(img2,(200,100),interpolation=cv2.INTER_AREA)

rows,cols,channels = img2.shape

if not capture.isOpened():
    print("Erro ao acessar o vídeo")
else:
    
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            roi = frame[0:rows, 0:cols]
            
            frame2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            ret, mask_inv = cv2.threshold(frame2gray, 125, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask_inv)
            
            frame1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

            frame2_fg = cv2.bitwise_and(img2,img2,mask = mask)
            dst = cv2.add(frame1_bg,frame2_fg)

            frame[0:rows, 0:cols ] = dst

            cv2.imshow('logo IF', frame)
          
            k=cv2.waitKey(20)
            if k == ord('q'):
                break
        else: break

capture.release()
cv2.destroyAllWindows()