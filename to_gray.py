import cv2
import os

def convert_to_grayscale(input_folder, output_folder):
    i = 30
    # Sprawdź, czy podane foldery istnieją
    if not os.path.exists(input_folder):
        print(f"Folder wejściowy '{input_folder}' nie istnieje.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Przetwarzaj każde zdjęcie w folderze wejściowym
    for filename in os.listdir(input_folder):
        i = i + 1
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Wczytaj obraz
            input_path = os.path.join(input_folder, filename)
            image = cv2.imread(input_path)



            # Zapisz obraz do folderu wyjściowego
            output_path = os.path.join(output_folder, f"{i}.bmp")
            cv2.imwrite(output_path, image)

            print(f"Przetworzono: {input_path} -> {output_path}")

if __name__ == "__main__":
    input_folder = "C:/Users/asus/Desktop/PSW/dataset/pos_out"
    output_folder = "C:/Users/asus/Desktop/Haar Training/training/positive/rawdata"

    convert_to_grayscale(input_folder, output_folder)
