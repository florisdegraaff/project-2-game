# Sprite classes
import pygame
from pkg.level1.settings import *
from pkg.foundation.display import *
from .interactionmark import *
from .jaildoor import *
from .mob import *
from .speechballoon import *
from .spritesheet import *
from .toilet import *
from .text import *

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

class Player(pygame.sprite.Sprite):
    def __init__(self, visible_speech_balloon):
        self.visible_speech_balloon = visible_speech_balloon
        self.spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        pygame.sprite.Sprite.__init__(self)
        self.walking = False
        self.can_walk = True
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
        self.walk_up_frames = [self.spritesheet.get_image(771, 324, 57, 82),
                               self.spritesheet.get_image(771, 407, 57, 82),
                               self.spritesheet.get_image(771, 324, 57, 82),
                               self.spritesheet.get_image(877, 83, 57, 82)]
        for frame in self.walk_up_frames:
            frame.set_colorkey(BLACK)


        self.walk_down_frames = [   self.spritesheet.get_image(889, 263, 57, 82),
                                    self.spritesheet.get_image(780, 174, 57, 82),
                                    self.spritesheet.get_image(889, 263, 57, 82),
                                    self.spritesheet.get_image(759, 84, 57, 82)]
        for frame in self.walk_down_frames:
            frame.set_colorkey(BLACK)


        self.walk_left_frames = [   self.spritesheet.get_image(664, 0, 57, 82),
                                    self.spritesheet.get_image(659, 246, 57, 82),
                                    self.spritesheet.get_image(664, 0, 57, 82),
                                    self.spritesheet.get_image(697, 164, 57, 82)]
        for frame in self.walk_left_frames:
            frame.set_colorkey(BLACK)


        self.walk_right_frames = [  self.spritesheet.get_image(635, 164, 57, 82),
                                    self.spritesheet.get_image(602, 82, 57, 82),
                                    self.spritesheet.get_image(635, 164, 57, 82),
                                    self.spritesheet.get_image(602, 0, 57, 82)]
        for frame in self.walk_right_frames:
            frame.set_colorkey(BLACK)

    def update(self):
        self.animate()
        self.speedx = 0
        self.speedy = 0
        self.keys = pygame.key.get_pressed()
        if (self.keys[pygame.K_UP] or self.keys[pygame.K_w]) and self.can_walk:
            if not self.visible_speech_balloon:
                self.speedy = -6
                self.speedx = 0
        if (self.keys[pygame.K_DOWN] or self.keys[pygame.K_s])  and self.can_walk:
            if not self.visible_speech_balloon:
                self.speedy = 6
                self.speedx = 0
        if (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a])  and self.can_walk:
            if not self.visible_speech_balloon:
                self.speedx = -6
                self.speedy = 0
        if (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d])  and self.can_walk:
            if not self.visible_speech_balloon:
                self.speedx = 6
                self.speedy = 0

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
