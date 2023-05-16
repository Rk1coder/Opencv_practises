import cv2

img = cv2.imread("klon.jpg")
# # print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

cv2.imshow("image",img)
cv2.imwrite("klon1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()