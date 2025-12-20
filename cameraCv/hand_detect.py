import cv2
import mediapipe as mp
import csv
import os

# ===== GESTURE LABEL =====
label = "C"   #  change this for each gesture

csv_file = "hand_landmarks.csv"
file_exists = os.path.isfile(csv_file)

# ===== CSV HEADER =====
header = []
for i in range(21):
    header += [f"x{i}", f"y{i}", f"z{i}"]
header.append("label")

# ===== CAMERA =====
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("❌ Camera open nahi ho raha")
    exit()

# ===== MEDIAPIPE =====
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# ===== CREATE CSV IF NOT EXISTS =====
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(header)

print("✅ Camera started")
print("👉 'S' = save landmark | ESC = exit")

# ===== LOOP =====
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb.flags.writeable = False
    results = hands.process(rgb)
    rgb.flags.writeable = True

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = []
            for lm in hand.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

    cv2.imshow("Phase 2 - Landmark Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    # ===== SAVE TO CSV =====
    if key == ord('s') and results.multi_hand_landmarks:
        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + [label])
        print(f"✅ Saved gesture: {label}")

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
