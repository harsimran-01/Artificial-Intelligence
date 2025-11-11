import cv2
import time

#cam = cv2.VideoCapture(0)
#time.sleep(1)
#_,img = cam.read()
#cv2.imwrite("imagefromCamera.jpg",img)
#cam.release()


cam = cv2.VideoCapture(0)
time.sleep(1)
while True:
    _,img = cam.read()
    cv2.imshow("camera feed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
   
cv2.imwrite("imagefromCamera.jpg",img)
cam.release()
cv2.destroyAllWindows()
