import pygame

WIDTH = 1280
HEIGHT = 720
pygame.init()
pygame.display.set_caption("Hello World!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

run:bool = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 0))
    pygame.display.update()