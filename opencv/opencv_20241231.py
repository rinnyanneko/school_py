import mediapipe as mp
import cv2
import pygame
import os

from pygame.examples.scrap_clipboard import screen

WIDTH = 600
HEIGHT = 800
pygame.init()
pygame.display.set_caption("Title")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load(os.path.join("..", "assets", "bliss.jpg")).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()

run = True
try:
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)


        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frameRGB)
        if results.multi_hand_landmarks:
            for handinfo in results.multi_hand_landmarks:
                print(handinfo.landmark[9].x * frame.shape[1], handinfo.landmark[9].y * frame.shape[0])


        cv2.imshow("Title", frame)
        if cv2.waitKey(5) == ord("c"):
            run = False
except Exception as e:
    print(e)
finally:
    cap.release()