# import cv2
#
# test = cv2.imread('test.jpg')
# gray_test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
# haar_plate = cv2.CascadeClassifier('PlateDetector.xml')
# detected_plate = haar_plate.detectMultiScale(gray_test, scaleFactor=1.1, minNeighbors=5)
#
# for (x,y,w,h) in detected_plate:
#     cv2.rectangle(gray_test, (x,y), (x+2, y+h), (250, 150, 50), 10)
#
# cv2.imshow(gray_test)

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/asus/Downloads/haarcascade_russian_plate_number.xml')
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 1)
print(faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()