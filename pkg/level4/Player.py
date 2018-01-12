import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

from pygame.math import Vector2

pygame = essentials.pygame

class Player:
    position = Vector2(100, 480)
    size = Vector2(100, 200)

    jump_counter = -20

    def __init__(self):
        self.rect = pygame.draw.rect(display.window, (0,0,0), pygame.Rect(self.position, self.size))

    def jump (self):
        self.size.y = 200
        self.position.y = 80 + self.jump_counter * self.jump_counter
        self.jump_counter+=1
        if self.jump_counter > 20:
            self.position.y = 480
            self.jump_counter = -20
            return False
        return True

    def crawl (self):
        self.size.y = 100
        self.position.y = 580

    def update (self):
        self.rect = pygame.draw.rect(display.window, (0,0,0), pygame.Rect(self.position, self.size))
        self.size.y = 200
        self.position.y = 480

    def end_game (self):
        self.position.x = self.position.x + 10

class Helicopter:
    position = Vector2(1480, 520)
    background_position = Vector2(1280, 0)

    def __init__(self):
        self.background = pygame.image.load("pkg/level4/background.png")
        self.chopper = pygame.image.load("pkg/level4/choppah.png")
        display.window.blit(self.chopper, self.position)

    def update(self):
        self.position.x = self.position.x - 10
        self.background_position.x = self.background_position.x - 18.6
        display.window.blit(self.background, self.background_position)
        display.window.blit(self.chopper, self.position)
