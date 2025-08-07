" Project: Face Detection App "

import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# load haar cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces_from_images(image_path):
     # load an image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors= 5, minSize= (30, 30))

    # draw rectangles around detected facesS
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y),(x + w, y + h), (0, 255, 0), 2)

    # show the image
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Face Detection")
    plt.axis('off')
    plt.show()

def detect_faces_from_webcam():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    fig, ax = plt.subplots()
    img_display = ax.imshow([[0]], cmap='gray')
    plt.axis('off')

    def update(frame):
        ret, frame = cap.read()
        if not ret:
            return
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        img_display.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return img_display,

    ani = FuncAnimation(fig, update, interval=50, blit=True)
    plt.show()

    cap.release()
    
print("Choose an option:")
print("1. Detect face from an image")
print("2. Detect face from webcam")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    image_path = input("Enter the path of the image: ")
    detect_faces_from_images(image_path)
elif choice == "2":
    detect_faces_from_webcam()
else:
    print("Invalid choice")

