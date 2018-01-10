# Sprite classes
import pygame
from settings import *

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()
    
    def get_image(self, x, y, width, height):
        # grabs an image out of a spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Walls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        #self.image.fill(RED)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Exits(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bed(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        #self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bars(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        #self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class InteractionMark(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Jaildoor(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.doorClosed = True
        self.image = self.game.spritesheet.get_image(642, 290, 15, 215)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 605
        self.rect.y = 263

        if self.doorClosed == False:
            self.rect.x = -100
       
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.walk_down_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = (width / 2)
        self.rect.y = (height / 2)
        self.speedx = 0
        self.speedy = 0

    def load_images(self):
        # Player walk sprites
        self.walk_up_frames = [self.game.spritesheet.get_image(417, 212, 57, 82),
                               self.game.spritesheet.get_image(358, 294, 57, 82),
                               self.game.spritesheet.get_image(417, 212, 57, 82),
                               self.game.spritesheet.get_image(348, 560, 57, 82)]
        for frame in self.walk_up_frames:
            frame.set_colorkey(BLACK)

        
        self.walk_down_frames = [self.game.spritesheet.get_image(469, 469, 57, 82),
                               self.game.spritesheet.get_image(476, 212, 57, 82),
                               self.game.spritesheet.get_image(469, 469, 57, 82),
                               self.game.spritesheet.get_image(525, 552, 57, 82)]
        for frame in self.walk_down_frames:
            frame.set_colorkey(BLACK)


        self.walk_left_frames = [self.game.spritesheet.get_image(339, 212, 57, 82),
                               self.game.spritesheet.get_image(62, 610, 57, 82),
                               self.game.spritesheet.get_image(339, 212, 57, 82),
                               self.game.spritesheet.get_image(296, 314, 57, 82)]
        for frame in self.walk_left_frames:
            frame.set_colorkey(BLACK)


        self.walk_right_frames = [self.game.spritesheet.get_image(0, 610, 57, 82),
                               self.game.spritesheet.get_image(348, 478, 57, 82),
                               self.game.spritesheet.get_image(0, 610, 57, 82),
                               self.game.spritesheet.get_image(348, 396, 57, 82)]
        for frame in self.walk_right_frames:
            frame.set_colorkey(BLACK)


    def update(self):
        self.animate()
        self.speedx = 0
        self.speedy = 0
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            self.speedy = -6
        if self.keys[pygame.K_DOWN]:
            self.speedy = 6
        if self.keys[pygame.K_LEFT]:
            self.speedx = -6
        if self.keys[pygame.K_RIGHT]:
            self.speedx = 6
        if self.keys[pygame.K_SPACE]:
            print("SPACE")
            
            
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        

    def animate(self):
        now = pygame.time.get_ticks()
        if self.speedx | self.speedy != 0:
            self.walking = True
        else:
            self.walking = False
        # walk animation
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_left_frames)
                if self.speedx > 0:
                    self.image = self.walk_right_frames[self.current_frame]
                if self.speedx < 0:
                    self.image = self.walk_left_frames[self.current_frame]
                if self.speedy < 0:
                    self.image = self.walk_up_frames[self.current_frame]
                if self.speedy > 0:
                    self.image = self.walk_down_frames[self.current_frame]

        