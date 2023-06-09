import cv2

cap = cv2.VideoCapture('Mushrooms.mp4')

new_width = 440
new_height = 180

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('Mushrooms1.mp4', fourcc, fps, (new_width, new_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized = cv2.resize(frame, (new_width, new_height))

    out.write(resized)

    cv2.imshow('IFMA', resized)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
