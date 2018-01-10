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
    def __init__(self, game, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((width, height))
        self.image = self.game.spritesheet.get_image(245, 212, 15, 49)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Jaildoor(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(992, 0, 15, 215)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 605
        self.rect.y = 263

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(664, 82, 57, 82)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Toilet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(393, 350, 69, 100)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class SpeechBalloon(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(0, 0, 600, 210)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def choose_scenario(self, game, reader, scenario):
        self.scenario = scenario
        self.amount_of_columns = len(reader[scenario - 1])
        self.current_row = scenario - 1
        game.visible_speech_balloon = True

class Text(pygame.sprite.Sprite):
    def __init__(self, game, highlighted_answer):
        pygame.sprite.Sprite.__init__(self)
        
        self.text_highlighted = 153, 153, 153
        self.text_not_highlighted = 219,219,219

        if game.speech_balloon_object.amount_of_columns == 1:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))

        if game.speech_balloon_object.amount_of_columns == 2:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))

        if game.speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 0:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))

        if game.speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 1:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            
        if game.speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 2:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))

        if game.speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 3:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))
       
        if game.speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 0:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if game.speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 1:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if game.speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 2:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
        
        if game.speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 3:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if game.speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 4:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 620))

        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 0:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 1:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))
    
        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 2:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))
            
        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 3:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))
            
        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 4:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if game.speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 5:
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            game.screen.blit(game.font.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_highlighted), (335, 650))

        if game.speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 1:
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 550))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 580))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 600))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 630))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][5], False, BLACK, self.text_not_highlighted), (335, 650))

        if game.speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 2:
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 550))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 580))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 600))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 630))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][5], False, BLACK, self.text_not_highlighted), (335, 650))
    
        if game.speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 3:
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 550))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 580))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 600))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][4], False, BLACK, self.text_highlighted), (335, 630))
            game.screen.blit(game.font2.render(game.reader[game.speech_balloon_object.current_row][5], False, BLACK, self.text_highlighted), (335, 650))

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
        self.walk_up_frames = [self.game.spritesheet.get_image(771, 324, 57, 82),
                               self.game.spritesheet.get_image(771, 407, 57, 82),
                               self.game.spritesheet.get_image(771, 324, 57, 82),
                               self.game.spritesheet.get_image(877, 83, 57, 82)]
        for frame in self.walk_up_frames:
            frame.set_colorkey(BLACK)

        
        self.walk_down_frames = [self.game.spritesheet.get_image(889, 263, 57, 82),
                               self.game.spritesheet.get_image(780, 174, 57, 82),
                               self.game.spritesheet.get_image(889, 263, 57, 82),
                               self.game.spritesheet.get_image(759, 84, 57, 82)]
        for frame in self.walk_down_frames:
            frame.set_colorkey(BLACK)


        self.walk_left_frames = [self.game.spritesheet.get_image(664, 0, 57, 82),
                               self.game.spritesheet.get_image(659, 246, 57, 82),
                               self.game.spritesheet.get_image(664, 0, 57, 82),
                               self.game.spritesheet.get_image(697, 164, 57, 82)]
        for frame in self.walk_left_frames:
            frame.set_colorkey(BLACK)


        self.walk_right_frames = [self.game.spritesheet.get_image(635, 164, 57, 82),
                               self.game.spritesheet.get_image(602, 82, 57, 82),
                               self.game.spritesheet.get_image(635, 164, 57, 82),
                               self.game.spritesheet.get_image(602, 0, 57, 82)]
        for frame in self.walk_right_frames:
            frame.set_colorkey(BLACK)

    def update(self):
        self.animate()
        self.speedx = 0
        self.speedy = 0
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            if self.game.visible_speech_balloon == False:
                self.speedy = -6
                self.speedx = 0
        if self.keys[pygame.K_DOWN]:
            if self.game.visible_speech_balloon == False:
                self.speedy = 6
                self.speedx = 0
        if self.keys[pygame.K_LEFT]:
            if self.game.visible_speech_balloon == False:
                self.speedx = -6
                self.speedy = 0
        if self.keys[pygame.K_RIGHT]:
            if self.game.visible_speech_balloon == False:
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