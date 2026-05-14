import os
import pyttsx3
import pygame
from pathlib import Path
from tools.check_requirement import check_and_install_libraries

class Config():

    check_and_install_libraries()

    # === Audio ===

    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 1.0)

    pygame.mixer.init()

    PLAY_SONGS:bool = True

    # === Haar classifiers ===

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

    # === Images folder ===

    ROOT_DIR = Path(__file__).resolve().parent

    ASSETS_DIR = ROOT_DIR / "assets"
    IMAGES_DIR = ASSETS_DIR / "images"
    SOUNDS_DIR = ASSETS_DIR / "sounds"

    GUNFIRE_SOUND_PATH = SOUNDS_DIR / "gunfire.wav"
    TONE_SOUND_PATH = SOUNDS_DIR / "tone.wav"

    IMAGE_FILES = sorted(IMAGES_DIR.iterdir())