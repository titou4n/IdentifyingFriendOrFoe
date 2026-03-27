import os
import time
from datetime import datetime

import pyttsx3
import cv2 as cv
from config import Config
import pygame

# python -m pip install pygame

config = Config()

def get_CascadeClassifier(name_haar):
        return cv.CascadeClassifier(cv.data.haarcascades + config.DICT_HAAR[name_haar])

def get_image_gray(image):
    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    if img_gray is None:
        print(f"[WARNING] Cannot read image: {image}, skipping.")
        return None
    return img_gray

def eye_and_face_detection(img_gray, face_rect_list):
    discharge_weapon = True
    for rect in face_rect_list:
        for (x, y, w, h) in rect:

            # Draw face rectangle (white)
            cv.rectangle(img_gray, (x, y), (x + w, y + h), 255, 2)

            # Search for eyes inside the face region
            rect_4_eyes = img_gray[y:y + h, x:x + w]
            eyes = config.eye_cascade.detectMultiScale(
                image=rect_4_eyes,
                scaleFactor=1.05,
                minNeighbors=2,
            )

            for (xe, ye, we, he) in eyes:
                print("Eyes detected.")

                # Draw eye rectangle (gray) inside the face region
                cv.rectangle(rect_4_eyes, (xe, ye), (xe + we, ye + he), 180, 2)

                # Draw circle around the eye center
                center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
                radius = int((we + he) / 3)
                cv.circle(rect_4_eyes, center, radius, 255, 2)

                discharge_weapon = False

            # Break after the first face that contains at least one eye
            if not discharge_weapon:
                break
    return discharge_weapon

def print_result(img_gray, image, discharge_weapon):

    #height, width = img_gray.shape
    height, width = img_gray.shape[:2]

    pygame.mixer.init()
    # -- Fire or stand down --
    if not discharge_weapon:
        pygame.mixer.music.load(config.tone_path)
        pygame.mixer.music.play()
        cv.imshow('Detected Faces', img_gray)
        cv.waitKey(2000)
        cv.destroyWindow('Detected Faces')
        time.sleep(5)
    else:
        print(f"No face in {image}. Discharging weapon!")
        cv.putText(
            img_gray, 'FIRE!',
            (int(width / 2) - 20, int(height / 2)),
            cv.FONT_HERSHEY_PLAIN, 3, 255, 3,
        )
        pygame.mixer.music.load(config.gunfire_path)
        pygame.mixer.music.play()
        cv.imshow('Mutant', img_gray)
        cv.waitKey(2000)
        cv.destroyWindow('Mutant')
        time.sleep(3)

def print_result_webcam(img_gray, image, discharge_weapon):

    #height, width = img_gray.shape
    height, width = img_gray.shape[:2]

    pygame.mixer.init()
    # -- Fire or stand down --
    if not discharge_weapon:
        pygame.mixer.music.load(config.tone_path)
        pygame.mixer.music.play()
    else:
        print(f"No face in {image}.")
        cv.putText(
            img_gray, 'FIRE!',
            (int(width / 2) - 20, int(height / 2)),
            cv.FONT_HERSHEY_PLAIN, 3, 255, 3,
        )
        pygame.mixer.music.load(config.gunfire_path)
        pygame.mixer.music.play()

def show_image(image):
    # Show raw image before detection
    cv.imshow(f'Motion detected {image}', image)
    cv.waitKey(2000)
    cv.destroyWindow(f'Motion detected {image}')

def main():
    for image in config.contents:
        print(f"\nMotion detected...{datetime.now()}")
        

        config.engine.say("You have entered an active fire zone. "
                    "Stop and face the gun immediately. "
                    "When you hear the tone, you have 5 seconds to pass.")
        #engine.runAndWait()
        time.sleep(3)

        img_gray = get_image_gray(image=image)
        #show_image(img_gray)

        # -- Face detection --
        face_rect_list = []
        face_rect_list.append(config.face_cascade.detectMultiScale(
            image=img_gray,
            scaleFactor=1.1,
            minNeighbors=5,
        ))

        # -- Eye detection + rectangle drawing --
        print(f"Searching {image} for eyes.")
        discharge_weapon = eye_and_face_detection(img_gray, face_rect_list)
        print_result(img_gray=img_gray, image=image, discharge_weapon=discharge_weapon)

    config.engine.stop()

def detectsFacesWebcam(name_haar="face_alt"):
    """Detects faces in real time using the webcam."""
 
    cap = cv.VideoCapture(0)
 
    if not cap.isOpened():
        print("[ERROR] Cannot open camera.")
        return
 
    print("[INFO] Camera started. Press 'q' to quit.")
 
    while True:
        ret, frame = cap.read()  # ret = bool, frame = image
 
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break
 
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
        cascade_classifier = get_CascadeClassifier(name_haar=name_haar)
        rects = cascade_classifier.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=3,
        )
 
        discharge_weapon = True
        # Draw a rectangle around each detected face
        for (x, y, w, h) in rects:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            discharge_weapon = False
 
        cv.imshow('Camera - detection', frame)
        print_result_webcam(img_gray=gray, image=frame, discharge_weapon=discharge_weapon)
 
        # Press 'q' to quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
 
    # Release resources outside the loop
    cap.release()
    cv.destroyAllWindows()
    print("[INFO] Camera released.")


if __name__ == "__main__":
    #main()
    #detectsFacesWebcam(name_haar="upper_body")
    detectsFacesWebcam()