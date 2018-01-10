# Mini Game 1
import pygame
import random
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        image_dir = path.join(self.dir, 'images')

        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(image_dir, SPRITESHEET))
        
        # load background
        self.background = pygame.image.load(path.join(image_dir, BACKGROUND)).convert()
        self.background_rect = self.background.get_rect()
        
        
    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bed = pygame.sprite.Group()
        self.bars = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.jaildoor = pygame.sprite.Group()
        self.interaction_mark = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player, self.walls, self.bed, self.bars, self.jaildoor, self.exits, self.interaction_mark)
        # upper wall in player cell
        wall1 = Walls(619, 0, 600, 50) 
        # right wall in player cell
        wall2 = Walls(1219, 0, 70, 706)
        # the bars in the other cell
        wall3 = Walls(198, 0, 15, 720)
        # the lowest wall in player cell
        wall4 = Walls(619, 705, 661, 15)
        # the bed object in player cell
        bedObject = Bed(994, 33, 210, 180)
        # the upper bars "object" in player cell
        barsObjectUp = Bars(605, 0, 15, 263)
        # the lower bars "object" in player cell
        barsObjectDown = Bars(605, 477, 15, 243)
        # the exit on the top
        exitUp = Exits(213, -70, 391, 5)
        # the exit on the down
        exitDown = Exits(213, 790, 391, 5)
        # the door of the player's cell
        jailDoor = Jaildoor(self)
        
        # the interaction mark for the bars in the player's cell
        self.mark1 = False
        self.interaction_mark1 = InteractionMark(585, 10, 0, 0)
        if self.mark1 == True:
            self.interaction_mark1 = InteractionMark(585, 10, 8, 8)
        # the interaction mark for the bed "object" in the player's cell
        self.mark2 = False
        self.interaction_mark2 = InteractionMark(960, 20, 0, 0)
        if self.mark2 == True:
            self.interaction_mark2= InteractionMark(960, 20, 8, 8)

        self.all_sprites.add(wall1, wall2, wall3, wall4, bedObject, barsObjectUp, barsObjectDown, jailDoor, exitUp, exitDown, self.interaction_mark1, self.interaction_mark2)
        self.walls.add(wall1, wall2, wall3, wall4)
        self.exits.add(exitUp, exitDown)
        self.bed.add(bedObject)
        self.bars.add(barsObjectUp, barsObjectDown, jailDoor)
        self.run()
        pass

    def run(self):
        # Game loop
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        self.all_sprites.update()
        hits_wall = pygame.sprite.spritecollide(self.player, self.walls, False)
        if hits_wall:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy

        hits_bed = pygame.sprite.spritecollide(self.player, self.bed, False)
        if hits_bed:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy
            self.interact = False
            self.mark2 = True
            print(self.interact)
            if self.player.keys[pygame.K_SPACE]:
                self.interact = True
                print(self.interact)

        hits_bars = pygame.sprite.spritecollide(self.player, self.bars, False)
        if hits_bars:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy
            self.interact = False
            self.mark1 = True
            print(self.interact)
            if self.player.keys[pygame.K_SPACE]:
                self.interact = True
                print(self.interact)                

        hits_jaildoor = pygame.sprite.spritecollide(self.player, self.jaildoor, False)
        if hits_jaildoor:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy


        hits_exit = pygame.sprite.spritecollide(self.player, self.exits, False)
        if hits_exit:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy
            pygame.quit()

        pass
    def events(self):
        # Game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
                    self.mark1 = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass
    def draw(self):
        # Game loop - draw
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
            
        pygame.display.update()    

    def show_start_screen(self):
        # start screen
        pass

game = Game()
game.show_start_screen()

while game.running:
    game.new()

pygame.quit()



