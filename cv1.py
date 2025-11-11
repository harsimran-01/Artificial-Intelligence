import cv2
img = cv2.imread("sample1.jpg")
cv2.imshow("First CV Image",img)
cv2.imwrite("FirstImage.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
