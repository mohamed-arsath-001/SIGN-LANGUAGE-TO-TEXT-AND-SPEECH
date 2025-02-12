import mediapipe as mp

mp_hands = mp.solutions.hands

def detect_hands(image):
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
        results = hands.process(image)
        if results.multi_hand_landmarks:
            return results.multi_hand_landmarks[0]
    return None