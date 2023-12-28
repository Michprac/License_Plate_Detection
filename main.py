import numpy as np
import cv2

plate_cascade = cv2.CascadeClassifier('C:/Users/asus/Desktop/PSW/haarcascade_russian_plate_number.xml')

img = cv2.imread('test2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width, _ = img.shape


plates = plate_cascade.detectMultiScale(gray, 1.2, 10)
print(plates)

blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (237, 227, 26), 2)
    blurred_img[y:y + h, x:x + w] = img[y:y + h, x:x + w]



cv2.imshow('img', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()