import pkg.foundation.essentials as essentials

pygame = essentials.pygame

from pygame.math import Vector2

import os

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, *groups):
        super(Player, self).__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("pkg/level2/images/player.png"))
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
