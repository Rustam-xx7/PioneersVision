import cv2
import mediapipe as mp
import numpy as np
import joblib
import time
import os

# ================= LOAD MODEL =================
MODEL_PATH = os.path.join("model", "asl_model.pkl")
model = joblib.load(MODEL_PATH)

# ================= MEDIAPIPE =================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

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
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand.landmark:
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

