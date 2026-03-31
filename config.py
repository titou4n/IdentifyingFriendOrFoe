import os
from datetime import datetime
# from playsound import playsound
import pyttsx3
import cv2 as cv
import pygame
from pathlib import Path

from check_requirement import check_and_install_libraries


class Config():

    check_and_install_libraries()

    #__Audio___
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 1.0)
    #engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    pygame.mixer.init()

    #___Haar_classifiers___
    #face_cascade_default = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    #eye_cascade  = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
    #face_cascade_alt = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    DICT_HAAR = {
        "eye": "haarcascade_eye.xml",
        "eye_glasses": "haarcascade_eye_tree_eyeglasses.xml",
        
        "face_alt": "haarcascade_frontalface_alt.xml",
        "face_alt2": "haarcascade_frontalface_alt2.xml",
        "face_alt_tree": "haarcascade_frontalface_alt_tree.xml",
        "face_default": "haarcascade_frontalface_default.xml",
        
        "full_body": "haarcascade_fullbody.xml",
        "lower_body": "haarcascade_lowerbody.xml",
        "upper_body": "haarcascade_upperbody.xml",
        
        "left_eye": "haarcascade_lefteye_2splits.xml",
        "right_eye": "haarcascade_righteye_2splits.xml",
        
        "profile_face": "haarcascade_profileface.xml",
        "smile": "haarcascade_smile.xml"
    }

    #___Images folder___
    os.chdir('corridor_5')
    contents = sorted(os.listdir())


    ROOT_DIR = Path(__file__).resolve().parent
    SOUNDS_FOLDER = ROOT_DIR / "sounds"

    gunfire_path = SOUNDS_FOLDER / "gunfire.wav"
    tone_path = SOUNDS_FOLDER / "tone.wav"