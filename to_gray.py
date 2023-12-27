import cv2
import os

def convert_to_grayscale(input_folder):
    i = 0
    all = 0
    # Sprawdź, czy podane foldery istnieją
    if not os.path.exists(input_folder):
        print(f"Folder wejściowy '{input_folder}' nie istnieje.")
        return

    all = len(os.listdir(input_folder))
    print(all)
    # Przetwarzaj każde zdjęcie w folderze wejściowym
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):

            face_cascade = cv2.CascadeClassifier('PlateDetector.xml')
            input_path = os.path.join(input_folder, filename)
            img = cv2.imread(input_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            plates = face_cascade.detectMultiScale(gray, 1.1, 10)
            if len(plates):
                i = i + 1

    print(f"Znaleziono: {i} / {all}")



if __name__ == "__main__":
    input_folder = "C:/Users/asus/Desktop/Images"

    convert_to_grayscale(input_folder)
