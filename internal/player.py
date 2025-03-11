from GameSprite import GSprite
import pygame
from settings import *
from collections import deque
class Hero(GSprite):
    def __init__(self, image_path, pos_x, pos_y, speed, size_x, size_y):
        super().__init__(image_path, pos_x, pos_y, speed, size_x, size_y)
        self.anim_walk = deque([pygame.transform.scale(pygame.image.load(f'assets/Solider/Soldier_1/walk/{i}.png'),(self.size_x,self.size_y)).convert_alpha() for i in range(7)])
        self.animation_count_walk = 0
        self.anim_walk_p = False
        self.anim_speed = 10
    def walk(self):
        key_presed = pygame.key.get_pressed()

        if key_presed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.anim_walk_p = True
        if key_presed[pygame.K_RIGHT] and self.rect.x + self.size_x <= 1000 :
            self.rect.x += self.speed
            self.anim_walk_p = True


        if key_presed[pygame.K_d] and self.rect.x + self.size_x <= 1000 :
            self.rect.x += self.speed
            self.anim_walk_p = True

        if key_presed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.anim_walk_p = True

        print(self.rect.x)
    def walk_anim(self):
        if self.anim_walk_p:
            self.image = self.anim_walk[0]
            if self.animation_count_walk < self.anim_speed:
                self.animation_count_walk += 1
            else:
                self.anim_walk.rotate()
                self.animation_count_walk = 0