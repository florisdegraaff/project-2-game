import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

pygame = essentials.pygame

class Guard:

    def __init__ (self):
        self.position = [1280, 480]
        self.size = (100, 200)

    def update (self):
        self.guard = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1]), self.size))
        self.position [0] -= 20

class Bullets:

    def __init__ (self):
        self.position = [1280, 280]
        self.size = (20, 20)

    def update (self):
        self.bullet1 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1]), self.size))
        self.bullet2 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1] + 100), self.size))
        self.bullet3 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1] + 200), self.size))
        self.position [0] -= 20
