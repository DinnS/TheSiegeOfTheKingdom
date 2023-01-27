import pygame
from pygame.math import Vector2

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.Surface((64,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))

        # movement
        self.pos = Vector2(self.rect.center)
        self.direction = Vector2()
        self.speed = 200

        # collisions
        #self.hitbox = self.rect.inflate()


    def input(self):
        keys = pygame.key.get_pressed()
        # move horizontal
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # move vertical
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0


    def movement(self,dt):
        # normalize
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.pos.y)


    def update(self,dt):
        self.input()
        self.movement(dt)
