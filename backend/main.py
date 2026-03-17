import cv2
from ai_modules.face_detection import detect_face
from ai_modules.eye_tracking import detect_eyes
from ai_modules.alert_system import show_alert

def run_proctoring():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    print("Camera started")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        frame = detect_face(frame)
        frame = detect_eyes(frame)
        frame = show_alert(frame, "AI Proctoring Active")

        cv2.imshow("AI Proctoring Dashboard", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_proctoring()
