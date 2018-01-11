import pkg.foundation.essentials as essentials

pygame = essentials.pygame

import os

class TopAndBottomWall(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super(TopAndBottomWall, self).__init__(*groups)
        self.image = pygame.image.load(os.path.join("pkg/level2/images/topandbottomwall.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
