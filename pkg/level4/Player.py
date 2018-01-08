from .. import essentials
from .. import display

pygame = essentials.pygame

class Player:
    position = (100, 480)
    size = (100, 200)

    jump_counter = -20

    def __init__(self):
        self.rect = pygame.draw.rect(display.window, (0,0,0), pygame.Rect(self.position, self.size))

    def jump (self):
        self.size = (100, 200)
        self.position = (100, 80 + self.jump_counter * self.jump_counter)
        self.jump_counter+=1
        if self.jump_counter > 20:
            self.position = (100, 480)
            self.jump_counter = -20
            return False
        return True

    def crawl (self):
        self.size = (100, 200)
        self.position = (100, 580)

    def update (self):
        self.rect = pygame.draw.rect(display.window, (0,0,0), pygame.Rect(self.position, self.size))
        self.size = (100, 200)
        self.position = (100, 480)
