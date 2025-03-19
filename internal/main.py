"""
главный файл , здесь я вызываю все модули делаю цикл и тд
"""
import pygame
from settings import *
from player import Hero
from  GameSprite import GSprite
from helper import resource_path
screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
bg = pygame.image.load(resource_path('assets/background/fon.jpg'))
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero(resource_path('assets/image/error.png'), WIGTH//2,(HEIGHT//7)*4,3,WIGTH//16,HEIGHT//5)
while True:
    screen.blit(bg, (0, 0))
    hero.reset(screen)
    hero.walk()
    hero.walk_anim_right()
    hero.walk_anim_left()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                exit()
        if e.type == pygame.VIDEORESIZE:
            HEIGHT = e.w
            bg = pygame.transform.scale(bg,(e.w,e.h))
    pygame.display.flip()
    clock.tick(FPS)