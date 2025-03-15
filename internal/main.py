import pygame
from settings import *
from player import Hero
from ground import Ground
from helper import resource_path
from  GameSprite import GSprite
screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
bg = pygame.image.load('assets/background/fon.jpg')
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero(resource_path('assets/image/error.png'), WIGTH//2,(HEIGHT//7)*4,3,WIGTH//16,HEIGHT//5)
grounds = Ground(resource_path('assets/floor/floor.png'), 0,(HEIGHT//7)*6,3,WIGTH,HEIGHT//5)
while True:
    screen.blit(bg, (0, 0))
    grounds.reset(screen)
    grounds.collide(hero)
    GRAVITY = grounds.gravity
    hero.reset(screen)


    hero.walk()
    hero.gravity_hero()
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