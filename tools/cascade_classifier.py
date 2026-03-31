import cv2 as cv
from config import Config

config = Config()

class MyCascadeClassifier():

    def __init__(self):
            pass
    
    def get_CascadeClassifier(self, name_haar):
        return cv.CascadeClassifier(cv.data.haarcascades + config.DICT_HAAR[name_haar])
    
    def eye_and_face_detection(self, img_gray) -> tuple[list, list]:
        # === Face detection ===
        face_cascade = self.get_CascadeClassifier(name_haar="face_default")
        eye_cascade = self.get_CascadeClassifier(name_haar="eye")

        faces = face_cascade.detectMultiScale(
            image=img_gray,
            scaleFactor=1.1,
            minNeighbors=5,
        )

        all_faces = []
        all_eyes = []

        for (x, y, w, h) in faces:
            all_faces.append((x, y, w, h))

            rect_4_eyes = img_gray[y:y + h, x:x + w]

            # === Eye detection ===
            eyes = eye_cascade.detectMultiScale(
                image=rect_4_eyes,
                scaleFactor=1.05,
                minNeighbors=2,
            )

            for (xe, ye, we, he) in eyes:
                all_eyes.append((xe, ye, we, he))

            # draw
            self.draw_circle_around_eyes(eyes, rect_4_eyes)

        return all_faces, all_eyes
    
    def just_find_eye_and_face_detection(self, img_gray) -> bool:
        face_rect_list = []
        cascade_classifier = self.get_CascadeClassifier(name_haar="face_default")
        face_rect_list.append(cascade_classifier.detectMultiScale(
            image=img_gray,
            scaleFactor=1.1,
            minNeighbors=5,
        ))

        find_eye = False
        for rect in face_rect_list:
            for (x, y, w, h) in rect:
                cv.rectangle(img=img_gray, pt1=(x, y), pt2=(x + w, y + h), color=255, thickness=2)

                rect_4_eyes = img_gray[y:y + h, x:x + w]
                eyes_cascadeClassifier = self.get_CascadeClassifier("eye")
                eyes = eyes_cascadeClassifier.detectMultiScale(
                    image=rect_4_eyes,
                    scaleFactor=1.05,
                    minNeighbors=2,
                )
                self.draw_circle_around_eyes(eyes, rect_4_eyes)
                find_eye = len(eyes)!=0
                
                if find_eye:
                    break

            if find_eye:
                break

        return find_eye
    
    def draw_circle_around_eyes(self, eyes, rect_4_eyes):
        for (xe, ye, we, he) in eyes:
            print("Eyes detected.")
            cv.rectangle(img=rect_4_eyes, pt1=(xe, ye), pt2=(xe + we, ye + he), color=180, thickness=2)
            center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
            radius = int((we + he) / 3)
            cv.circle(img=rect_4_eyes, center=center, radius=radius, color=255, thickness=2)