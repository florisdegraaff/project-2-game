from pkg.foundation.essentials import *

from .spritesheet import *
from .settings import *

class SpeechBalloon(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame = essentials.pygame
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        self.image = spritesheet.get_image(0, 0, 600, 210)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def choose_scenario(self, visible_speech_balloon, reader, scenario):
        self.scenario = scenario
        self.amount_of_columns = len(reader[scenario - 1])
        self.current_row = scenario - 1
        visible_speech_balloon = True
