import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    retval, image = cap.read()

    if retval:
        faces = classifier.detectMultiScale(image)

        if len(faces)>0:
            face = faces[0]
            x, y, w, h = face

            cv2.imshow("my photo", image[x:x+w, y:y+h])

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.jpg", image)


cap.release()
cv2.destroyAllWindows()