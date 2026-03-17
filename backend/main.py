import cv2
from ai_modules.face_detection import detect_face
from ai_modules.eye_tracking import detect_eyes
from ai_modules.alert_system import show_alert

def run_proctoring():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print("AI Proctoring System Started")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect face
        frame, faces = detect_face(frame)

        # Detect eyes
        frame, eyes = detect_eyes(frame)

        # --------------------
        # Calculate Risk Score
        # --------------------

        risk_score = 0
        alert = "Monitoring Candidate"

        if faces == 0:
            risk_score += 2
            alert = "Face Not Visible"

        elif faces > 1:
            risk_score += 3
            alert = "Multiple Persons Detected"

        if eyes == 0 and faces == 1:
            risk_score += 1
            alert = "Eyes Not Visible"

        # --------------------
        # Risk Level
        # --------------------

        if risk_score == 0:
            risk_level = "SAFE"
            color = (0,200,0)

        elif risk_score <= 2:
            risk_level = "LOW RISK"
            color = (0,255,255)

        elif risk_score <= 4:
            risk_level = "SUSPICIOUS"
            color = (0,165,255)

        else:
            risk_level = "HIGH RISK"
            color = (0,0,255)

        frame = show_alert(frame, alert)

        height, width, _ = frame.shape

        start_x = width - 260
        start_y = height - 140

        cv2.rectangle(frame,
                      (start_x - 10, start_y - 40),
                      (width - 10, height - 10),
                      (255,255,255),
                      -1)

        cv2.putText(frame,
                    "AI Proctoring Active",
                    (start_x, start_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1)

        cv2.putText(frame,
                    f"Faces Detected: {faces}",
                    (start_x, start_y + 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1)

        cv2.putText(frame,
                    f"Risk Score: {risk_score}",
                    (start_x, start_y + 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1)

        cv2.putText(frame,
                    f"Risk Level: {risk_level}",
                    (start_x, start_y + 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2)

        cv2.putText(frame,
                    "Modules Active:",
                    (start_x, start_y + 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1)

        cv2.putText(frame,
                    "Face Detection | Eye Tracking",
                    (start_x, start_y + 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1)

        cv2.imshow("AI Proctoring Dashboard", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_proctoring()
