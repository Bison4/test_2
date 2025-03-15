import pygame
from bullet import Bullet
from enemy import Enemy
from ground import Ground
from player import Hero
from settings import *
from effects import Blud
from effects import Corpse
from helper import resource_path

screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
bg = pygame.image.load(resource_path("assets/background/fon.jpg"))
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
pygame.display.set_caption('Niger')
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero("assets/Solider/Soldier_1/main.png", WIGTH//2,(HEIGHT//7)*4,3,WIGTH//16,HEIGHT//5, GRAVITY_SREED, FIRE)
grounds = Ground("assets/floor/floor.png", 0,(HEIGHT//7)*6,3,WIGTH,HEIGHT//5)
def collise_Z(enemy,bullet):
    if bullet.rect.colliderect(enemy.rect):
        enemy.rect.x = 0
        enemy.rect.y = 0

bullet_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
blood_group = pygame.sprite.Group()
corpse_group = pygame.sprite.Group()

zombie_event = pygame.USEREVENT + 2
pygame.time.set_timer(zombie_event, 2000)



while True:
    screen.blit(bg, (0, 0))

    grounds.reset(screen)
    grounds.collide(hero)
    HERO_GRAVITY = grounds.gravity
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
        if e.type == pygame.MOUSEBUTTONDOWN:
            FIRE = True
        if e.type == zombie_event:
            z = Enemy("assets/image/error.png", (0, 0), (200, 400), hero, 1, grounds, GRAVITY_SREED, Blud, blood_group, Corpse, corpse_group)
            zombie_group.add(z)




    zombie_list = zombie_group.sprites()


    if FIRE:
        bul = Bullet("assets/image/bullett.png",(hero.rect.center),(20,4), hero, zombie_list[0])
        bullet_group.add(bul)
    hero.fire_check(FIRE)
    hero.shot_anim_right()
    hero.shot_anim_left()


    bullet_group.draw(screen)
    bullet_group.update()

    blood_group.draw(screen)
    corpse_group.draw(screen)
    zombie_group.draw(screen)
    zombie_group.update()
    FIRE = False
    pygame.display.flip()
    clock.tick(FPS)
