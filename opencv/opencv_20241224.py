import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hand = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
#    try:
        ret, frame = cap.read()
#        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(frame_RGB)
        print(result.multi_hand_landmarks)
        cv2.imshow("TETORIS", frame)
        if cv2.waitKey(3) == ord('q'):
            break
#    except Exception as e:
#        print(e)
#        break