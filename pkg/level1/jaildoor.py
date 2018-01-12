from pkg.foundation.essentials import *

from .spritesheet import *
from .settings import *

class Jaildoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame = essentials.pygame
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        self.image = spritesheet.get_image(992, 0, 15, 215)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 605
        self.rect.y = 263
