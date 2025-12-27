import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision
from mediapipe import Image, ImageFormat
import numpy as np
import joblib
import time
import os

# ================= LOAD MODEL =================
# MODEL_PATH = os.path.join("model", "asl_model.pkl")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "asl_model.pkl")
model = joblib.load(MODEL_PATH)

# ================= MEDIAPIPE =================
HAND_TASK_PATH = os.path.join(os.path.dirname(__file__), "model", "hand_landmarker.task")
if not os.path.exists(HAND_TASK_PATH):
    os.makedirs(os.path.dirname(HAND_TASK_PATH), exist_ok=True)
    import urllib.request
    url = (
        "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
        "hand_landmarker/float16/latest/hand_landmarker.task"
    )
    urllib.request.urlretrieve(url, HAND_TASK_PATH)

base_options = mp_python.BaseOptions(model_asset_path=HAND_TASK_PATH)
options = mp_vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.6,
    min_hand_presence_confidence=0.6,
    min_tracking_confidence=0.6
)
landmarker = mp_vision.HandLandmarker.create_from_options(options)

# ================= TEXT STATE =================
sentence = ""
last_pred = None
last_time = 0
COOLDOWN = 1.0

# ================= CAMERA =================
cap = cv2.VideoCapture(0)

print("👉 Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = Image(image_format=ImageFormat.SRGB, data=rgb)
    results = landmarker.detect(mp_image)

    if results.hand_landmarks:
        for hand in results.hand_landmarks:
            h, w = frame.shape[:2]
            landmarks = []
            for lm in hand:
                # Draw simple points for feedback
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 3, (255, 0, 0), -1)
                landmarks.extend([lm.x, lm.y, lm.z])

            if len(landmarks) == 63:
                X = np.array(landmarks).reshape(1, -1)
                pred = model.predict(X)[0]

                current_time = time.time()
                if pred != last_pred and (current_time - last_time) > COOLDOWN:
                    last_pred = pred
                    last_time = current_time

                    if pred == "space":
                        sentence += " "
                    elif pred == "del":
                        sentence = sentence[:-1]
                    elif pred != "nothing":
                        sentence += pred

                    with open("recognized_text.txt", "w", encoding="utf-8") as f:
                        f.write(sentence)

    cv2.putText(frame, f"Text: {sentence}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("ASL Gesture to Text", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

