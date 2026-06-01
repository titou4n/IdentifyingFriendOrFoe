from datetime import datetime

from config import Config
from tools.cascade_classifier import MyCascadeClassifier
from tools.tools_image import ToolsImage
from detects_faces_webcam import detectsFacesWebcam


config = Config()
cascade_classifier = MyCascadeClassifier()
image_tools = ToolsImage()


def main() -> None:
    for image in config.IMAGE_FILES:
        print(f"\nProcessing image: {image} at {datetime.now()}")

        config.engine.say(
            "You have entered an active fire zone. "
            "Stop and face the gun immediately. "
            "When you hear the tone, you have 5 seconds to pass."
        )

        gray_image = image_tools.get_image_gray(image=image)
        print(f"Searching {image} for eyes and faces.")

        has_faces_detected = cascade_classifier.just_find_eye_and_face_detection(
            img_gray=gray_image
        )

        image_tools.print_result(
            img_gray=gray_image,
            image=image,
            discharge_weapon=not has_faces_detected,
            play_songs=config.PLAY_SONGS,
        )

    config.engine.stop()


if __name__ == "__main__":
    while True:
        choice = input("Enter 1 for image processing or 2 for webcam: ")
        if choice == "1":
            main()
        elif choice == "2":
            detectsFacesWebcam()
        else:
            pass