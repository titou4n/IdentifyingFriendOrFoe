import cv2 as cv
from tools.cascade_classifier import MyCascadeClassifier
from tools.tools_image import ToolsImage


my_cascade_classifier = MyCascadeClassifier()
tools_image = ToolsImage()

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
 
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
        cascade_classifier = my_cascade_classifier.get_CascadeClassifier(name_haar=name_haar)
        rects = cascade_classifier.detectMultiScale(
            img_gray,
            scaleFactor=1.2,
            minNeighbors=3,
        )

        # Draw a rectangle around each detected face
        color = (255, 255, 255)
        for (x, y, w, h) in rects:
            cv.rectangle(img=img_gray,
                            pt1=(x, y),
                            pt2=(x + w, y + h),
                            color=color,
                            thickness=2)

        discharge_weapon = not my_cascade_classifier.eye_and_face_detection(img_gray)
 
        cv.imshow('Camera - detection', frame)
        tools_image.print_result_webcam(img_gray=img_gray, image=frame, discharge_weapon=discharge_weapon)
 
        # Press 'q' to quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
 
    # Release resources outside the loop
    cap.release()
    cv.destroyAllWindows()
    print("[INFO] Camera released.")