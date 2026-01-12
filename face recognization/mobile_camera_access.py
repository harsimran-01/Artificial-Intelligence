import cv2
import imutils

url = "http://192.168.1.2:8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()

    if not ret:
        print("⚠ Lost frame, reconnecting…")
        cap = cv2.VideoCapture(url)
        continue

    frame = imutils.resize(frame, width=450)
    cv2.imshow("CameraFeed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
