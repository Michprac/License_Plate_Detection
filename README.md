# Application for detection license plate on the image

The aim of this project was to create an application that allows you to find license plates in a selected photo.

This application serves two main functions:
- easy way to upload a photo using the graphical interface
  - Tkinter library used
- license plate detection along with the detected text on this plate
  - OpenCV and Tesseract libraries used

# The preview of the application while working

<p align = "center">
  <img src ="/images/main_screen.png" width="400">
  <img src ="/images/process_screen.png" width="400" >
</p>

On the images above you can see two sample photos that show the application: immediately after launch and during sample detection (test photo taken from the Internet).

It should also be noted that after pressing the *Find plate* button, another window with an enlarged image will pop up, in order to better observe the result.

# Mode of action

Before starting detection, the user must upload two files: the image on which he wants to perform detection and a special Haar cascade that is required for detection. There is an example xml model in the OpenCV library, which was tested in the photo above.

<p align = "center">
  <img src ="/images/detection_screen.png" width="200" >
</p>

Also, the user can select the two parameters shown in the above photo to slightly adjust the license plate detection. These two parameters concern the *detectMultiScale* method used in the OpenCV library.

After setting the parameters and uploading the appropriate files, the user can click the *Find plate* button, which will result in detection. It is important to note that the rest of the image apart from the detected board will be blurred, which helps to focus on a specific place in the image. If the program does not detect anything, the user will only get a blurry photo as a result.
