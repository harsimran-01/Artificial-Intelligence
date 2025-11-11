
#detecting face and saving those images into the databases or separate folder

import cv2
import os

dataset = "dataset"
name = "champ"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)


alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)
count = 1
while count<31:
    print(count)
    _,img = cam.read()
    grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImage,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceOnly = grayImage[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),faceOnly)
        count+=1
        
    cv2.imshow("face detection",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
print("Image captured Successfully")
cam.release()
cv2.destroyAllWindows()





#basic code for detecting face and making rectangle on that 

#import cv2

#alg = "haarcascade_frontalface_default.xml"

#haar_cascade = cv2.CascadeClassifier(alg)

#cam = cv2.VideoCapture(0)
#while True:
 #   _,img = cam.read()
  #  grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   # face = haar_cascade.detectMultiScale(grayImage,1.3,4)
    #for(x,y,w,h) in face:
     #   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imshow("face detection",img)
    #key = cv2.waitKey(1)
    #if key == ord('q'):
     #   break

#cam.release()
#cv2.destroyAllWindows()

