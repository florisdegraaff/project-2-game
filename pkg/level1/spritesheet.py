import pkg.foundation.essentials as essentials

from .spritesheet import *

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        global essentials
        self.pygame = essentials.pygame
        self.spritesheet = self.pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # grabs an image out of a spritesheet
        image = self.pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image
