import cv2
img = cv2.imread("sample1.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianBlurImg.jpg",gaussianBlurImg)
cv2.imshow("Blur image",gaussianBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
