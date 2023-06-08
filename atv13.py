import cv2,sys

cap = cv2.VideoCapture("IFMA.mp4")
if not cap.isOpened():
    print("Erro ao abrir o video")
    sys.exit(0)

face_cascade = cv2.CascadeClassifier('classificadores/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    people_counter = len(faces)
    cv2.putText(img, 'Pessoas: {}'.format(people_counter), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    cv2.imshow('Webcam', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
