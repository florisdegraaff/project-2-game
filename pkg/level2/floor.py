import pkg.foundation.essentials as essentials

pygame = essentials.pygame

import pygame

import os

class Floor(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super(Floor, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join("pkg/level2/images/floor.png"))
        print (self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
#test
