import cv2
import pytesseract

# Initializing path of the tesseract and path of the cascade xml
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
plate_cascade = cv2.CascadeClassifier('C:/Users/asus/Desktop/PSW/haarcascade_russian_plate_number.xml')

img = cv2.imread('test.jpg')
height, width, _ = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plates = plate_cascade.detectMultiScale(gray, 1.2, 10)
print(plates)

blured_img = cv2.GaussianBlur(img, (15, 15), 0)
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (237, 227, 26), 2)
    # inserting detected region on the blured image
    blured_img[y:y+h, x:x+w] = img[y:y+h, x:x+w]
    text = pytesseract.image_to_string(blured_img[y:y+h, x:x+w])
    cv2.putText(blured_img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (237, 227, 26), 2)

cv2.imshow('Detection', blured_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

