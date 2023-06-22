import cv2
import time

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
class_names = []
desired_class = "person"
people_counter = 0

with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

cap = cv2.VideoCapture("IFMA.mp4")

net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)

model.setInputParams(size=(416, 416), scale=1/255)

while True:
    
    _, frame = cap.read()
    
    start = time.time()
    
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)
    
    end = time.time()
    people_counter = 0
    for(classid, score, box) in zip(classes, scores, boxes):
        if class_names[classid] == desired_class:
            color = COLORS[int(classid) % len(COLORS)]
            label = f"{class_names[classid]} : {score:.1%}"
            cv2.rectangle(frame, box, color, 2)
            people_counter = len(boxes)
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        cv2.putText(frame, f"Quantidade de Pessoas: {people_counter}", (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
               
    cv2.imshow("YOLO", frame)
    
    k = cv2.waitKey(1)
    
    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()