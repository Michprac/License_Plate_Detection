import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

# Variables for storing paths of the cascade xml and image for detection
filename_xml = ""
filename_image = ""


def search_xml():
    global filename_xml
    filename_xml = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("xml files", "*.xml"),
                                                                                          ("all files", "*.*")))
    text_variable_xml.set(os.path.basename(filename_xml))
    if filename_xml:
        xml_label.config(fg="green")

def search_image():
    global filename_image

    filename_image = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpg files", "*.jpg"),
                                                                                        ("png files", "*.png"),
                                                                                        ("all files", "*.*")))
    image = Image.open(filename_image)

    if image:
        image_label.config(fg="green")
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


def find_plate():
    global filename_xml, filename_image
    # Initializing path of the tesseract and path of the cascade xml
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    plate_cascade = cv2.CascadeClassifier(filename_xml)

    img = cv2.imread(filename_image)
    height, width, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(gray,
                                            float(text_variable_scale_factor.get()),
                                            int(text_variable_min_neigh.get())
                                            )
    # print(plates)

    blured_img = cv2.GaussianBlur(img, (15, 15), 0)
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (237, 227, 26), 2)
        # inserting detected region on the blured image
        blured_img[y:y + h, x:x + w] = img[y:y + h, x:x + w]
        text = pytesseract.image_to_string(img[y:y + h, x:x + w])
        cv2.putText(blured_img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (237, 227, 26), 2)

    image_PIL = Image.fromarray(cv2.cvtColor(blured_img, cv2.COLOR_BGR2RGB))

    new_height = 350
    new_width = int(width * new_height / height)

    image_PIL = image_PIL.resize((new_width, new_height))

    photo = ImageTk.PhotoImage(image_PIL)
    start_x = 0
    if new_width < 700:
        start_x = int((700 - new_width) / 2)

    canv2.create_image(start_x, 0, anchor="nw", image=photo)
    canv2.image = photo



    cv2.imshow('Detection', blured_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


window = tk.Tk()

text_variable_image = tk.StringVar(value="choose image")
text_variable_xml = tk.StringVar(value="choose xml")

text_variable_scale_factor = tk.StringVar(value="1.2")
text_variable_min_neigh = tk.StringVar(value="10")

window_height = 750
window_width = 970
d_x = 100
d_y = 50

window.title('License Plate Detector')
window.geometry(f"{window_height}x{window_width}+{d_x}+{d_y}")
window.minsize(window_width, window_height)
window.maxsize(window_width, window_height)




tk.Label(window, text="--FILES--", font=("Arial", 30)).grid(row=0, column=1, stick="nwe", padx=5)

search_btn_xml = tk.Button(window, text="Open cascade", font="Arial", command=search_xml)
search_btn_xml.grid(row=1, column=1, stick="nwe", padx=5)

xml_label = tk.Label(window, textvariable=text_variable_xml, font=("Arial", 10), fg="red")
xml_label.grid(row=2, column=1, stick="nwe", padx=5)

search_btn_image = tk.Button(window, text="Open image", font="Arial", command=search_image)
search_btn_image.grid(row=3, column=1, stick="nwe", padx=5)

image_label = tk.Label(window, textvariable=text_variable_image, font=("Arial", 10), fg="red")
image_label.grid(row=4, column=1, stick="nwe", padx=5)



tk.Label(window, text="--Detection--", font=("Arial", 30)).grid(row=6, column=1, stick="nwe", padx=5)

detect_btn = tk.Button(window, text="Find plate", font="Arial", command=find_plate)
detect_btn.grid(row=7, column=1, stick="nwe", padx=5)

tk.Label(window, text="Scale Factor:", font=("Arial", 15)).grid(row=8, column=1, stick="nwe", padx=5)
entry_scale_factor = tk.Entry(window, font=("Arial", 10, 'normal'), textvariable=text_variable_scale_factor)
entry_scale_factor.grid(row=9, column=1, stick="nwe", padx=5)

tk.Label(window, text="Min Neighbours:", font=("Arial", 15)).grid(row=10, column=1, stick="nwe", padx=5)
entry_min_neigh = tk.Entry(window, font=("Arial", 10, 'normal'), textvariable=text_variable_min_neigh)
entry_min_neigh.grid(row=11, column=1, stick="nwe", padx=5)


canv1 = tk.Canvas(window, width=700, height=350, bg='white')
canv1.grid(row=0, column=0, rowspan=5, stick="n")

canv2 = tk.Canvas(window, width=700, height=350, bg='white')
canv2.grid(row=6, column=0, rowspan=6, pady=25, stick="n")





window.mainloop()


