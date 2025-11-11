import cv2
import imutils
img = cv2.imread("sample1.jpg")
resizeImg = imutils.resize(img,width=200,height=200)
cv2.imwrite("resizedImage.jpg",resizeImg)
cv2.imshow("resize CV Image",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
