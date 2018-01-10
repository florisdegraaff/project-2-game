import pkg.foundation.essentials as essentials

pygame = essentials.pygame

import os

class HorizontalWall(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super(HorizontalWall, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join("pkg/level2/images/horizontal_wall.png"))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
