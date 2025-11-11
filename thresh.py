import cv2
img = cv2.imread("sample1.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImg,70,255,cv2.THRESH_BINARY)[1]
cv2.imshow("ThreshHold Image",threshImg)
cv2.imwrite("thresholf_image.jpg",threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
