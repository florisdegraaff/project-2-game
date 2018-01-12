import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

pygame = essentials.pygame

class Guard:

    def __init__ (self):
        self.image = [
            pygame.image.load('pkg/level4/images/copLeft2.png'),
            pygame.image.load('pkg/level4/images/copLeft1.png'),
            pygame.image.load('pkg/level4/images/copLeft3.png'),
            pygame.image.load('pkg/level4/images/copLeft1.png')
        ]
        self.walkTimer = essentials.timer(0.125)
        self.currentSprite = 0
        self.position = [1280, 480]
        self.size = (100, 200)

    def update (self):
        if (self.walkTimer.check_timer()):
            self.walkTimer = essentials.timer (0.125)
            if self.currentSprite < 3:
                self.currentSprite+=1
            else:
                self.currentSprite = 0
        self.guard = pygame.draw.rect(display.window, (122,122,122), pygame.Rect((self.position[0], self.position[1]), self.size))
        display.window.blit(self.image[self.currentSprite], self.position)
        self.position [0] -= 20

class Bullets:

    def __init__ (self):
        self.position = [1280, 280]
        self.size = (10, 10)

    def update (self):
        self.bullet1 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1]), self.size))
        self.bullet2 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1] + 100), self.size))
        self.bullet3 = pygame.draw.rect(display.window, (0,0,0), pygame.Rect((self.position[0], self.position[1] + 200), self.size))
        self.position [0] -= 20
