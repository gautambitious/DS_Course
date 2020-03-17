import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        continue
    cv2.imshow("Video Frame", frame)
    cv2.imshow("Gray Video", frame2)
    # Wait for user input and close when "q" is pressed
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
