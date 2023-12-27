import cv2

test = cv2.imread('test.png')
gray_test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
haar_plate = cv2.CascadeClassifier('path/to/xml')
detected_plate = haar_plate.detectMultiScale(gray_test, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in detected_plate:
    cv2.rectangle(test, (x,y), (x+2, y+h), (250, 150, 50), 10)

cv2.imshow(test)