import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

pygame = essentials.pygame

from pygame.math import Vector2

import os

from itertools import cycle

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, *groups):
        super(Player, self).__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        #for moving right animation
        images = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/right1", "pkg/level2/images/right2", "pkg/level2/images/right1", "pkg/level2/images/right3")]
        self.images = cycle(images)
        self.image = next(self.images)
        #timer for animated sprite
        self.timer = 0
        self.frame_duration = 150 #about 15 frames at 60 fps
        #for moving left animation
        images2 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/left1", "pkg/level2/images/left2", "pkg/level2/images/left1", "pkg/level2/images/left3")]
        self.images2 = cycle(images2)
        self.image = next(self.images2)
        #for moving up animation
        images3 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/up1", "pkg/level2/images/up2", "pkg/level2/images/up1", "pkg/level2/images/up3")]
        self.images3 = cycle(images3)
        self.image = next(self.images3)
        #for moving down animation
        images4 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/down1", "pkg/level2/images/down2", "pkg/level2/images/down1", "pkg/level2/images/down3")]
        self.images4 = cycle(images4)
        self.image = next(self.images4)

        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

    #timer for moving right animation
    def counter(self, dt):
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        if key[pygame.K_d]:
            self.timer += dt
        while self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.image = next(self.images)
    #timer for moving left animation
    def counter2(self, dt):
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        if key[pygame.K_a]:
            self.timer += dt
        while self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.image = next(self.images2)
    #timer for moving up animation
    def counter3(self, dt):
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        if key[pygame.K_w]:
            self.timer += dt
        while self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.image = next(self.images3)
    #timer for moving down animation
    def counter4(self, dt):
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        if key[pygame.K_s]:
            self.timer += dt
        while self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.image = next(self.images4)
