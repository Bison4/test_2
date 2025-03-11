import pygame
from settings import *
from player import Hero
from  GameSprite import GSprite
screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
bg = pygame.image.load('assets/background/fon.jpg')
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero('assets/error.png', WIGTH//2,(HEIGHT//7)*4,3,WIGTH//16,HEIGHT//5)
while True:
    screen.blit(bg, (0, 0))
    hero.reset(screen)
    hero.walk()
    hero.walk_anim()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                exit()
        if e.type == pygame.VIDEORESIZE:

            bg = pygame.transform.scale(bg,(e.w,e.h))
    pygame.display.flip()
    clock.tick(FPS)