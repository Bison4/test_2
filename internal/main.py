import pygame
from settings import *
screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
bg = pygame.image.load('assets/background/fon.jpg')
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
while True:
    screen.blit(bg, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                exit()
        if e.type == pygame.VIDEORESIZE:

            bg = pygame.transform.scale(bg,(e.w,e.h))
    pygame.display.flip()
    clock.tick(FPS)