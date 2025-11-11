import cv2
import imutils
img = cv2.imread("sample1.jpg")
resizeImg = imutils.resize(img,width=400,height=400)
cv2.rectangle(resizeImg,(120,20),(220,220),(0,255,0),2)
cv2.putText(resizeImg,"hello my first text",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
cv2.imshow("Rectangle on the Image",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

