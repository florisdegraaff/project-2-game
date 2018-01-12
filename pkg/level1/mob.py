from pkg.foundation.essentials import *

from .spritesheet import *
from .settings import *

class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame = essentials.pygame
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        self.image = spritesheet.get_image(664, 82, 57, 82)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
