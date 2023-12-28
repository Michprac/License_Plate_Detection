import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

# # Initializing path of the tesseract and path of the cascade xml
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# plate_cascade = cv2.CascadeClassifier('C:/Users/asus/Desktop/PSW/haarcascade_russian_plate_number.xml')
#
# img = cv2.imread('test.jpg')
# height, width, _ = img.shape
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# plates = plate_cascade.detectMultiScale(gray, 1.2, 10)
# print(plates)
#
# blured_img = cv2.GaussianBlur(img, (15, 15), 0)
# for (x, y, w, h) in plates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (237, 227, 26), 2)
#     # inserting detected region on the blured image
#     blured_img[y:y+h, x:x+w] = img[y:y+h, x:x+w]
#     text = pytesseract.image_to_string(blured_img[y:y+h, x:x+w])
#     cv2.putText(blured_img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (237, 227, 26), 2)
#
# cv2.imshow('Detection', blured_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

filename_xml = ""
filename_image = ""





def search_xml():
    global filename_xml
    filename_xml = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("xml files", "*.xml"),
                                                                                          ("all files", "*.*")))

    print(filename_image)

def search_image():
    global filename_image

    filename_image = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpg files", "*.jpg"),
                                                                                        ("png files", "*.png"),
                                                                                        ("all files", "*.*")))
    image = Image.open(filename_image)
    # Show with label what image have you picked
    text_variable_image.set(os.path.basename(image.filename))

    width, height = image.size

    new_height = 350
    new_width = int(width * new_height / height)

    image = image.resize((new_width, new_height))

    photo = ImageTk.PhotoImage(image)
    start_x = 0
    if new_width < 700:
        start_x = int((700 - new_width) / 2)

    canv1.create_image(start_x, 0, anchor="nw", image=photo)
    canv1.image = photo




window = tk.Tk()

text_variable_image = tk.StringVar(value="choose image")

text_variable_xml = tk.StringVar(value="choose xml")

window_height = 750
window_width = 1000
d_x = 100
d_y = 50

window.title('License Plate Detector')
window.geometry(f"{window_height}x{window_width}+{d_x}+{d_y}")
window.minsize(window_width, window_height)
window.maxsize(window_width, window_height)




tk.Label(window, text="--FILES--", font=("Arial", 30)).grid(row=0, column=1, stick="nwe", padx=5)

search_btn_xml = tk.Button(window, text="Open cascade", font="Arial", command=search_xml)
search_btn_xml.grid(row=1, column=1, stick="nwe", padx=5)

xml_label = tk.Label(window, textvariable=text_variable_xml, font=("Arial", 10))
xml_label.grid(row=2, column=1, stick="nwe", padx=5)

search_btn_image = tk.Button(window, text="Open image", font="Arial", command=search_image)
search_btn_image.grid(row=3, column=1, stick="nwe", padx=5)

image_label = tk.Label(window, textvariable=text_variable_image, font=("Arial", 10))
image_label.grid(row=4, column=1, stick="nwe", padx=5)



canv1 = tk.Canvas(window, width=700, height=350, bg='white')
canv1.grid(row=0, column=0, rowspan=5, stick="n")

canv2 = tk.Canvas(window, width=700, height=350, bg='white')
canv2.grid(row=6, column=0, rowspan=5, pady=25, stick="n")





window.mainloop()


