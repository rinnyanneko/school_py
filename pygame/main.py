import pygame
import os

WIDTH = 1280
HEIGHT = 720
pygame.init()
pygame.display.set_caption("Hello World!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(os.path.join("assets", "bliss.jpg")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mouse = pygame.image.load(os.path.join("assets", "nachoneko.png")).convert_alpha()
run:bool = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets", "mouse.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
mice = Player()
all_sprite = pygame.sprite.Group()
all_sprite.add(mice)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(114514)
    screen.blit(background, (0, 0))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(mouse, (mouse_x - (mouse.get_width() / 2), mouse_y - (mouse.get_height() / 2)))
    all_sprite.draw(screen)
    pygame.display.update()