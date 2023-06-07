import cv2

capture = cv2.VideoCapture("IFMA.mp4")

if not capture.isOpened():
    print("Erro ao abrir o arquivo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            canny = cv2.Canny(frame,100,200)
            cv2.imshow('Canny', canny)
            
            k = cv2.waitKey(20)
            if k == ord("q"):
                break
        else:
            break

capture.release()
cv2.destroyAllWindows()