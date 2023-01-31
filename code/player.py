import pygame
from pygame.math import Vector2

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((64,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (pos[0],pos[1]))

        # movement
        self.pos = Vector2(self.rect.center)
        self.direction = Vector2()
        self.speed = 200


        # collisions
        #self.hitbox = self.rect.inflate()

        # background size
        self.background = pygame.image.load('../graphics/map.png')
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()

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

    def restrict(self):
        if self.rect.left < 0:
            self.pos.x = 0 + self.rect.width / 2
            # self.hitbox.left = 640
            self.rect.left = 0
        if self.rect.right > self.background_width:
            self.pos.x = self.background_width - self.rect.width / 2
            # self.hitbox.left = 640
            self.rect.right = self.background_width

        if self.rect.top < 0:
            self.pos.y = 0 + self.rect.height / 2
            self.rect.top = 0
        if self.rect.bottom > self.background_height:
            self.pos.y = self.background_height - self.rect.height / 2
            #  self.hitbox.centery = self.rect.centery
            self.rect.bottom = self.background_height


    def update(self,dt):
        self.input()
        self.movement(dt)
        self.restrict()
