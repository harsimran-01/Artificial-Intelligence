import cv2, numpy, os

haar_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
dataset = 'dataset'
print('Training..')

(images, labels, names, id) = ([], [], {}, 0)
(width, height) = (130, 100)

for (subdirs, dirs, files) in os.walk(dataset):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dataset, subdir)

        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)

            img = cv2.imread(path, 0)
            if img is None:
                continue   # Skip broken images

            # ✔ FIX — Resize all images so they have same shape
            img = cv2.resize(img, (width, height))

            images.append(img)
            labels.append(id)

        id += 1

# ✔ Now conversion to numpy works
images = numpy.array(images)
labels = numpy.array(labels)

print("Training data loaded:")
print("Total images:", len(images))
print("Total labels:", len(labels))
print("Names:", names)

# Train model
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# Start camera
webcam = cv2.VideoCapture(0)
cnt = 0

while True:
    ret, img = webcam.read()
    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (width, height))

        prediction = model.predict(face_resize)

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if prediction[1] < 800:
            name = names[prediction[0]]
            cv2.putText(img, f'{name}-{prediction[1]:.0f}', (x-10, y-10),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
            print(name)
            cnt = 0
        else:
            cnt += 1
            cv2.putText(img, 'Unknown', (x-10, y-10),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))

    cv2.imshow('Face Recognition OpenCV', img)

    if cv2.waitKey(10) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
