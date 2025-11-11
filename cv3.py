import cv2
img = cv2.imread("sample2.jpg")
print(img.size)
print(img.shape)
print(img.dtype)
                 
cv2.imshow("Image",img)

print("converting into greyscale")
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("sample2_gray.jpg",grayImage)
cv2.imshow("image",grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
