import cv2 as cv
import pygame
from config import Config


class ToolsImage():
    def __init__(self):
        self.config = Config()

    def get_image_gray(self, image):
        img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
        if img_gray is None:
            print(f"[WARNING] Cannot read image: {image}, skipping.")
            return None
        return img_gray

    def print_result(self, img_gray, image, discharge_weapon, play_songs:bool = True) -> None:

        #height, width = img_gray.shape
        height, width = img_gray.shape[:2]

        if play_songs:
            pygame.mixer.init()

        # -- Fire or stand down --
        if not discharge_weapon:
            if play_songs:
                pygame.mixer.music.load(self.config.tone_path)
                pygame.mixer.music.play()
            cv.imshow('Detected Faces', img_gray)
            cv.waitKey(2000)
            cv.destroyWindow('Detected Faces')
            return

        print(f"No face in {image}. Discharging weapon!")
        cv.putText(
            img_gray, 'FIRE!',
            (int(width / 2) - 20, int(height / 2)),
            cv.FONT_HERSHEY_PLAIN, 3, 255, 3,
        )
        if play_songs:
            pygame.mixer.music.load(self.config.gunfire_path)
            pygame.mixer.music.play()
        cv.imshow('Mutant', img_gray)
        cv.waitKey(2000)
        cv.destroyWindow('Mutant')

    def print_result_webcam(self, img_gray, image, discharge_weapon:bool, play_songs:bool = True) -> None:

        #height, width = img_gray.shape
        height, width = img_gray.shape[:2]

        if play_songs:
            pygame.mixer.init()

        # -- Fire or stand down --
        if not discharge_weapon:
            if play_songs:
                pygame.mixer.music.load(self.config.tone_path)
                pygame.mixer.music.play()
            return

        cv.putText(
            img_gray, 'FIRE!',
            (int(width / 2) - 20, int(height / 2)),
            cv.FONT_HERSHEY_PLAIN, 3, 255, 3,
        )

        if play_songs:
            pygame.mixer.music.load(self.config.gunfire_path)
            pygame.mixer.music.play()

    def show_image(self, image):
        # Show raw image before detection
        cv.imshow(f'Motion detected {image}', image)
        cv.waitKey(2000)
        cv.destroyWindow(f'Motion detected {image}')