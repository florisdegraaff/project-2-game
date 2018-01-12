import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

from pygame.math import Vector2

pygame = essentials.pygame

class Player:
    position = Vector2(100, 480)
    size = Vector2(100, 200)

    jump_counter = -20

    def __init__(self):
        self.isCrawling = False
        self.rect = pygame.draw.rect(display.window, (122, 122, 122), pygame.Rect(self.position, self.size))
        self.image = [
            pygame.image.load('pkg/level4/images/1.walkRight.png'),
            pygame.image.load('pkg/level4/images/2.walkRight.png'),
            pygame.image.load('pkg/level4/images/3.walkRight.png'),
            pygame.image.load('pkg/level4/images/4.walkRight.png')
        ]
        self.crawlImages = [
            pygame.image.load('pkg/level4/images/1.crawl.png'),
            pygame.image.load('pkg/level4/images/2.crawl.png'),
            pygame.image.load('pkg/level4/images/3.crawl.png'),
            pygame.image.load('pkg/level4/images/4.crawl.png')
        ]
        self.walkTimer = essentials.timer(0.125)
        self.currentSprite = 0

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
        self.isCrawling = True
        self.size.y = 100
        self.position.y = 580


    def update (self):
        if (self.walkTimer.check_timer()):
            self.walkTimer = essentials.timer (0.125)
            if self.currentSprite < 3:
                self.currentSprite+=1
            else:
                self.currentSprite = 0

        self.rect = pygame.draw.rect(display.window, (122, 122, 122), pygame.Rect(self.position, self.size))
        if self.isCrawling:
            display.window.blit(self.crawlImages[self.currentSprite], self.position)
        else:
            display.window.blit(self.image[self.currentSprite], self.position)
        self.size.y = 200
        self.position.y = 480
        self.isCrawling = False

    def end_game (self):
        self.position.x = self.position.x + 10

class Helicopter:
    position = Vector2(1480, 520)
    background_position = Vector2(1280, 0)

    def __init__(self):
        self.background = pygame.image.load("pkg/level4/images/background.png")
        self.chopper = pygame.image.load("pkg/level4/images/choppah.png")
        display.window.blit(self.chopper, self.position)

    def update(self):
        self.position.x = self.position.x - 10
        self.background_position.x = self.background_position.x - 18.6
        display.window.blit(self.background, self.background_position)
        display.window.blit(self.chopper, self.position)
