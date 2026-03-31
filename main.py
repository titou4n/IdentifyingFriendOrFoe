import time
from datetime import datetime

from config import Config
from tools.cascade_classifier import MyCascadeClassifier
from tools.tools_image import ToolsImage
from more_about_project.more_code_main import detectsFacesWebcam

config = Config()
my_cascade_classifier = MyCascadeClassifier()
tools_image = ToolsImage()


def main():
    for image in config.contents:
        print(f"\nMotion detected...{datetime.now()}")
        

        config.engine.say("You have entered an active fire zone. "
                    "Stop and face the gun immediately. "
                    "When you hear the tone, you have 5 seconds to pass.")
        #engine.runAndWait()
        time.sleep(3)

        img_gray = tools_image.get_image_gray(image=image)

        # -- Eye detection + rectangle drawing --
        print(f"Searching {image} for eyes.")

        #list_faces, list_eyes = my_cascade_classifier.eye_and_face_detection(img_gray)
        #discharge_weapon = len(list_eyes) == 0

        discharge_weapon = not my_cascade_classifier.just_find_eye_and_face_detection(img_gray=img_gray)

        tools_image.print_result(img_gray=img_gray, image=image, discharge_weapon=discharge_weapon, play_songs=False)

    config.engine.stop()

if __name__ == "__main__":
    main()
    #detectsFacesWebcam(name_haar="full_body")
    #detectsFacesWebcam()
    #detectsFacesWebcam()