"""
Тут класс для создания игрока
"""
from GameSprite import GSprite
import pygame
from settings import *
from helper import resource_path
from collections import deque
class Hero(GSprite):
    def __init__(self, image_path, pos_x, pos_y, speed, size_x, size_y):
        """
        добавляем необходимые переменные
        """
        super().__init__(image_path, pos_x, pos_y, speed, size_x, size_y)

        self.WIGTH = WIGTH
        self.anim_walk_right = deque([pygame.transform.scale(pygame.image.load(resource_path(f'assets/Solider/Soldier_1/walk/right/{i}.png')),(self.size_x,self.size_y)).convert_alpha() for i in range(7)])
        self.anim_walk_left = deque([pygame.transform.scale(pygame.image.load(resource_path(f'assets/Solider/Soldier_1/walk/left/{i}.png')),(self.size_x,self.size_y)).convert_alpha() for i in range(7)])
        self.animation_count_walk_l = 0

        self.animation_count_walk = 0
        self.anim_walk_p_r = False
        self.anim_walk_p_l = False

        self.anim_speed = 10
    def walk(self):
        """
        управление спрайтом
        """
        self.anim_walk_p_r = False
        self.anim_walk_p_l = False
        key_presed = pygame.key.get_pressed()

        if key_presed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.anim_walk_p_l = True
        if key_presed[pygame.K_RIGHT] and self.rect.x + self.size_x <= self.WIGTH :
            self.rect.x += self.speed
            self.anim_walk_p_r = True


        if key_presed[pygame.K_d] and self.rect.x + self.size_x <= self.WIGTH :
            self.rect.x += self.speed
            self.anim_walk_p_r = True

        if key_presed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.anim_walk_p_l = True


    def walk_anim_right(self):
        """
        анимация хотьбы на право спрайт
        """
        if self.anim_walk_p_r:
            self.image = self.anim_walk_right[0]
            if self.animation_count_walk < self.anim_speed:
                self.animation_count_walk += 1
            else:
                self.anim_walk_right.rotate()
                self.animation_count_walk = 0
    def walk_anim_left(self):
        """
        анимация хотьбы на лево спрайт
        """
        if self.anim_walk_p_l:
            self.image = self.anim_walk_left[0]
            if self.animation_count_walk_l < self.anim_speed:
                self.animation_count_walk_l += 1
            else:
                self.anim_walk_left.rotate()
                self.animation_count_walk_l = 0