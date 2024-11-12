import pygame
import os

WIDTH = 1280
HEIGHT = 720
pygame.init()
pygame.display.set_caption("Hello World!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(os.path.join("assets", "bliss.jpg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
run:bool = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(114514)
    screen.blit(background, (0, 0))
    pygame.display.update()