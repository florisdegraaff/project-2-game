from pkg.foundation.essentials import *

from .spritesheet import *
from .settings import *

class InteractionMark(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        global essentials
        pygame = essentials.pygame
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        self.image = pygame.Surface((width, height))
        self.image = spritesheet.get_image(245, 212, 15, 49)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
