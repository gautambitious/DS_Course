import cv2

img = cv2.imread("./mario.png")
cv2.imshow("Super Mario", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
