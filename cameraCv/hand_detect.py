import cv2
import mediapipe as mp
import os

# ===== SET GESTURE NAME HERE =====
gesture_name = "hello"
save_dir = os.path.join("dataset", gesture_name)
os.makedirs(save_dir, exist_ok=True)

print("Saving to:", os.path.abspath(save_dir))

# ===== CAMERA =====
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

# ===== MEDIAPIPE =====
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

count = 0
hand_crop = None   # 🔴 IMPORTANT

while True:
    success, frame = cap.read()
    if not success:
        print("❌ Frame read failed")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            x_list = []
            y_list = []

            for lm in hand.landmark:
                x_list.append(int(lm.x * w))
                y_list.append(int(lm.y * h))

            xmin, xmax = min(x_list), max(x_list)
            ymin, ymax = min(y_list), max(y_list)

            padding = 20
            xmin = max(0, xmin - padding)
            ymin = max(0, ymin - padding)
            xmax = min(w, xmax + padding)
            ymax = min(h, ymax + padding)

            hand_crop = frame[ymin:ymax, xmin:xmax]

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            if hand_crop is not None and hand_crop.size > 0:
                cv2.imshow("Hand Crop", hand_crop)

    cv2.imshow("Phase 1 - Hand Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    # ===== PRESS 'S' TO SAVE IMAGE =====
    if key == ord('s'):
        print("Crop shape:", None if hand_crop is None else hand_crop.shape)

        if hand_crop is not None and hand_crop.size > 0:
            img_path = os.path.join(save_dir, f"{count}.jpg")
            saved = cv2.imwrite(img_path, hand_crop)

            if saved:
                print("✅ Really Saved:", img_path)
                count += 1
            else:
                print("❌ Save failed")
        else:
            print("⚠ Hand crop empty – not saved")

    # ===== ESC TO EXIT =====
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


