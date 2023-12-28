import numpy as np
import cv2

plate_cascade = cv2.CascadeClassifier('C:/Users/asus/Desktop/PSW/haarcascade_russian_plate_number.xml')

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width, _ = img.shape


plates = plate_cascade.detectMultiScale(gray, 1.2, 10)
print(plates)
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (237, 227, 26), 2)


    roi_mask = np.zeros((height, width), dtype=np.uint8)
    roi_mask[y:y + h, x:x + w] = 255
    outside_roi_mask = cv2.bitwise_not(roi_mask)

    # Utwórz obraz poza ROI
    outside_roi_image = cv2.bitwise_and(img, img, mask=outside_roi_mask)

    blurred_roi = cv2.GaussianBlur(outside_roi_image, (15, 15), 0)

    blurred_roi[y:y + h, x:x + w] = img[y:y + h, x:x + w]

    cv2.imshow('img', blurred_roi)


cv2.waitKey(0)
cv2.destroyAllWindows()