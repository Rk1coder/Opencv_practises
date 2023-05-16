import cv2

# video dosyası
cap = cv2.VideoCapture("antalya.mp4")

# webcam
# cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    # webcam
    # frame = cv2.flip(frame, 1)

    cv2.imshow("Antalya", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()