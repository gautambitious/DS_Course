import cv2
import numpy as np

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    faces = classifier.detectMultiScale(frame)
    if ret:
        if len(faces) > 1:
            faces = sorted(faces, key=lambda item: item[2] * item[3], reverse=True)
            x, y, w, h = faces[0]
            act = frame[y:y + h, x:x + w]
            act = cv2.resize(act, (200, 200))
            cv2.imshow("Video", act)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
