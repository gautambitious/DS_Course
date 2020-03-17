import cv2

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)
        faces = sorted(faces, key=lambda item: -(item[1] * item[3]))

        if len(faces) >= 2:
            face1 = faces[0]
            face2 = faces[1]
            x1, y1, w1, h1 = face1
            x2, y2, w2, h2 = face2

            cut1 = image[y1:y1 + h1, x1:x1 + w1]
            cut2 = image[y2:y2 + h2, x2:x2 + w2]

            t_cut1 = cv2.resize(cut1, (w2, h2))
            t_cut2 = cv2.resize(cut2, (w1, h1))

            cut1[:] = t_cut2
            cut2[:] = t_cut1

            cv2.imshow("my window", image)

    key = cv2.waitKey(1)

    if ord("q") == key:
        break

cap.release()
cv2.destroyAllWindows()
