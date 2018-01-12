import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

# Mini Game 1
import pygame
import random
import csv

from .sprites import *
from .settings import *
from os import path

class Game:
    def __init__(self):
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(FONT, 19)
        self.font2 = pygame.font.Font(FONT, 13)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.runs = True
        self.running = True
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        image_dir = path.join(self.dir, 'images')
        script_dir = path.join(self.dir, 'scripts')
        music_dir = path.join(self.dir, 'music')

        # load spritesheet image
        self.spritesheet = Spritesheet(path.join(image_dir, SPRITESHEET))

        # load game background
        self.background = pygame.image.load(path.join(image_dir, BACKGROUND)).convert()
        self.background_rect = self.background.get_rect()

        # load start screen
        self.start_screen = pygame.image.load(path.join(image_dir, START_SCREEN)).convert()
        self.start_screen_rect = self.start_screen.get_rect()

        # load instructions screen
        self.instructions_screen = pygame.image.load(path.join(image_dir, INSTRUCTIONS)).convert()
        self.instructions_screen_rect = self.instructions_screen.get_rect()

        # load music
        pygame.mixer.music.load(path.join(music_dir, MUSIC))
        pygame.mixer.music.play(-1, 0.0)

        # load script
        with open(path.join(script_dir, SCRIPT)) as csv_file:
            self.reader = list(csv.reader(csv_file, delimiter = ';'))
            self.total_rows = len(self.reader)

        #for row in range(0, self.total_rows):
        #    print('Scenario', row + 1, 'bevat', len(self.reader[row]), 'kolom(men):', self.reader[row])

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bed = pygame.sprite.Group()
        self.bars = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.jaildoor = pygame.sprite.Group()
        self.interaction_mark = pygame.sprite.Group()
        self.toilet = pygame.sprite.Group()
        self.player = Player(self)
        self.mob = pygame.sprite.Group()
        self.speech_balloon = pygame.sprite.Group()
        self.text = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.walls, self.bed, self.bars, self.jaildoor, self.exits, self.interaction_mark, self.toilet, self.mob, self.speech_balloon, self.text)
        self.visible_speech_balloon = False
        self.multiple_choice_answers = False
        self.highlighted_answer = 0
        self.highlighted_answer_minimum_boundary = 0
        self.highlighted_answer_maximum_boundary = 0
        self.remove_textbox = False
        self.key_obtained = False
        self.toilet_scenario = 1
        self.bed_scenario = 2
        self.mob_scenario = 14
        self.start_screen_visible = True
        self.current_screen = 0

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
        self.jailDoor = Jaildoor(self)
        # the guy in the other cell
        self.mob1 = Mob(self, 130, 360)
        # the toilet in the player's cell
        self.toilet1 = Toilet(self, 700, 50)
        # the toilet in the other cell
        self.toilet2 = Toilet(self, 70, 50)
        # the interaction mark for the bars in the player's cell
        self.interaction_mark1 = InteractionMark(self, 150, 300, 8, 8)
        # the interaction mark for the bed "object" in the player's cell
        self.interaction_mark2= InteractionMark(self, 960, 5, 8, 8)
        # the interaction mark for the toilet
        self.interaction_mark3= InteractionMark(self, 700, 5, 8, 8)
        # the interaction mark for the unlocked door
        self.interaction_mark4= InteractionMark(self, 575, 280, 8, 8)
        # the speech balloon
        self.speech_balloon_object = SpeechBalloon(self, 300, 490, 300, 300)

        self.all_sprites.add(wall1, wall2, wall3, wall4, bedObject, barsObjectUp, barsObjectDown, self.jailDoor, exitUp, exitDown, self.toilet1, self.toilet2, self.mob1)
        self.walls.add(wall1, wall2, wall3, wall4)
        self.exits.add(exitUp, exitDown)
        self.bed.add(bedObject)
        self.bars.add(barsObjectUp, barsObjectDown, self.jailDoor)
        self.toilet.add(self.toilet1, self.toilet2)
        self.speech_balloon.add(self.speech_balloon_object)
        self.run()

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

        if self.player.speedx or self.player.speedy > 0:
            self.all_sprites.remove(self.interaction_mark1, self.interaction_mark2, self.interaction_mark3, self.interaction_mark4)
            self.all_sprites.remove(game.speech_balloon)

        # for interaction with the bed "object"
        if self.player.rect.x >= 930 and self.player.rect.y <= 222:
            self.interact = False
            if self.player.keys[pygame.K_SPACE]:
                self.interact = True
                if self.bed_scenario == 2:
                    self.multiple_choice_answers = True
                    self.highlighted_answer = 4
                    self.highlighted_answer_minimum_boundary = 4
                    self.highlighted_answer_maximum_boundary = 5
                self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

        # for interaction with the toilet
        if (self.player.rect.x >= 640 and self.player.rect.x <= 772) and self.player.rect.y <= 150:
            self.interact = False
            if self.player.keys[pygame.K_SPACE]:
                self.interact = True
                self.speech_balloon_object.choose_scenario(self, self.reader, self.toilet_scenario)

        # for interaction with the bars of the player's cell
        if self.player.rect.x == 622:
            if self.player.keys[pygame.K_SPACE]:
                if self.key_obtained == True:
                    self.all_sprites.remove(self.bars)
                    self.bars.remove(self.jailDoor)
                elif self.key_obtained == False:
                    self.interact = True
                    self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)


        hits_wall = pygame.sprite.spritecollide(self.player, self.walls, False)
        if hits_wall:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy

        hits_bed = pygame.sprite.spritecollide(self.player, self.bed, False)
        if hits_bed:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy

            if self.player.speedx == 0:
                self.all_sprites.add(self.interaction_mark2)
                self.interact = False

            if self.player.speedy == 0:
                self.all_sprites.add(self.interaction_mark2)
                self.interact = False


        hits_bars = pygame.sprite.spritecollide(self.player, self.bars, False)
        if hits_bars:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy

            if self.key_obtained == False:
                self.interact = False

                if self.player.speedx == 0:
                    self.all_sprites.add(self.interaction_mark1)

                if self.player.speedy == 0:
                    self.all_sprites.add(self.interaction_mark1)
                    if self.player.keys[pygame.K_SPACE]:
                        #self.key_obtained = False
                        self.interact = True
            if self.key_obtained == True:
                self.all_sprites.remove(self.bars)
                self.bars.remove(self.jailDoor)

        hits_jaildoor = pygame.sprite.spritecollide(self.player, self.jaildoor, False)
        if hits_jaildoor:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy


        hits_toilet = pygame.sprite.spritecollide(self.player, self.toilet, False)
        if hits_toilet:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy
            if self.player.speedx == 0:
                self.all_sprites.add(self.interaction_mark3)
                self.interact = False

            if self.player.speedy == 0:
                self.all_sprites.add(self.interaction_mark3)
                self.interact = False

        hits_exit = pygame.sprite.spritecollide(self.player, self.exits, False)
        if hits_exit:
            self.player.rect.x = self.player.rect.x - self.player.speedx
            self.player.rect.y = self.player.rect.y - self.player.speedy
            return True

    def events(self):
        # Game loop - events
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                    self.runs = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.visible_speech_balloon == True:
                        if self.multiple_choice_answers == True:
                            if self.highlighted_answer > self.highlighted_answer_minimum_boundary:
                                self.highlighted_answer -= 1
                if event.key == pygame.K_DOWN:
                    if self.visible_speech_balloon == True:
                        if self.multiple_choice_answers == True:
                            if self.highlighted_answer < self.highlighted_answer_maximum_boundary:
                                self.highlighted_answer += 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    #print(self.speech_balloon_object.scenario)
                    #print(self.speech_balloon_object.current_row)
                    #print(self.highlighted_answer)
                    if self.current_screen <= 1:
                        self.current_screen += 1

                    if self.visible_speech_balloon == True:
                        if self.speech_balloon_object.scenario == 1: # I don't have to go...
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 2 and self.highlighted_answer == 4: # Do you want to play a game?;Answer 3 questions...;and I'll hand over the key --> Yes
                            self.bed_scenario = 3
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 2 and self.highlighted_answer == 5: # Do you want to play a game?;Answer 3 questions...;and I'll hand over the key --> No
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 3: # Here is my first question:;The person who knows he uses;it, doesn't know he uses it.;What is it?
                            self.bed_scenario = 4
                            self.multiple_choice_answers = True
                            self.highlighted_answer = 1
                            self.highlighted_answer_minimum_boundary = 1
                            self.highlighted_answer_maximum_boundary = 4
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 4 and self.highlighted_answer != 4: # Insurance;Necktie;Sugar;Coffin
                            self.bed_scenario = 5
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 4 and self.highlighted_answer == 4: # Insurance;Necktie;Sugar;Coffin
                            self.bed_scenario = 6
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 5: # WRONG!;Get used to being here,;cause you're going to be;here for a while...
                            self.bed_scenario = 3
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 6: # That's correct.;Here's my next question:
                            self.bed_scenario = 7
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 7: # Have you ever heard of a;dyslexic Satanist?
                            self.bed_scenario = 8
                            self.multiple_choice_answers = True
                            self.highlighted_answer = 1
                            self.highlighted_answer_minimum_boundary = 1
                            self.highlighted_answer_maximum_boundary = 4
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 8 and self.highlighted_answer != 2: # They prey to Christ;He sold his soul to Santa;There are none;No
                            self.bed_scenario = 9
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 8 and self.highlighted_answer == 2: # They prey to Christ;He sold his soul to Santa;There are none;No
                            self.bed_scenario = 10
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 9: # You're wrong!;I guess you're not so smart;...
                            self.bed_scenario = 7
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 10: #  Okay. For my final game,;I want you to insult the;other inmate's mother.
                            self.bed_scenario = 11
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 11: # We're gonna torture him;with the infamous your momma jokes.
                            self.bed_scenario = 12
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 12: # Unfortunately for you,;I only know the setups,;you're gonna have to come;up with the punchlines
                            self.bed_scenario = 13
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 13: # Go talk to the other inmate.
                            self.bed_scenario = 10
                            self.mob_scenario = 15
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 14: # Go away.;I have nothing to say.
                            self.mob_scenario = 14
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 15: # Okay, here goes nothing... *
                            self.mob_scenario = 16
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 16: # HEY YOU!;YO' MOMMA'S SO FAT...
                            self.mob_scenario = 17
                            self.multiple_choice_answers = True
                            self.highlighted_answer = 1
                            self.highlighted_answer_minimum_boundary = 1
                            self.highlighted_answer_maximum_boundary = 3
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 17 and self.highlighted_answer != 2: # ...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...SHE HAS MORE FOLDS,;THAN AN ORIGAMI ACCORDEON!;...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!
                            self.mob_scenario = 18
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 17 and self.highlighted_answer == 2: # ...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...SHE HAS MORE FOLDS,;THAN AN ORIGAMI ACCORDEON!;...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!
                            self.mob_scenario = 19
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 18: # Stop talking trash!;You suck at this!
                            self.mob_scenario = 15
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 19: # Not a word about my mother!;She's a saint.
                            self.mob_scenario = 20
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 20: # YO' MOMMA'S SO RADIANT...
                            self.mob_scenario = 21
                            self.multiple_choice_answers = True
                            self.highlighted_answer = 1
                            self.highlighted_answer_minimum_boundary = 1
                            self.highlighted_answer_maximum_boundary = 3
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 21 and self.highlighted_answer != 1: # ...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!;...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!
                            self.mob_scenario = 22
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 21 and self.highlighted_answer == 1: # ...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!;...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!
                            self.mob_scenario = 23
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 22: # You ain't hurtin nobody,;you little bitch!
                            self.mob_scenario = 15
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 23: # Ahhh, it hurts...;IT HURTS!
                            self.mob_scenario = 24
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 24: # YO' MOMMA'S SO PUNCTUAL...
                            self.mob_scenario = 25
                            self.multiple_choice_answers = True
                            self.highlighted_answer = 1
                            self.highlighted_answer_minimum_boundary = 1
                            self.highlighted_answer_maximum_boundary = 3
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 25 and self.highlighted_answer != 2: # ...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...THE ONLY TIME SHE'S LOW;IS AT A LIMBO CONTEST!
                            self.mob_scenario = 26
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 25 and self.highlighted_answer == 2: # ...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...THE ONLY TIME SHE'S LOW;IS AT A LIMBO CONTEST!
                            self.mob_scenario = 27
                            self.multiple_choice_answers = False
                            self.highlighted_answer = 0
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.mob_scenario)

                        elif self.speech_balloon_object.scenario == 26: # You had your chance,;now FUCK OFF!
                            self.mob_scenario = 15
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 27: # Enough, enough!; I'm suffocating...;sob.. sob... *
                            self.mob_scenario = 28
                            self.bed_scenario = 30
                            self.speech_balloon_object.choose_scenario(self, self.reader, 29)

                        elif self.speech_balloon_object.scenario == 28: # I'm done talking to you;Leave me alone...
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 29: # Now to claim the key;and get the fuck outta here! *
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 30: # Man...;I had the time of my life!!;Didn't know you had it in ya!
                            self.bed_scenario = 31
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 31: # Unfortunately for you,;I don't have the key on me,;but I'm sure that you little;POTTY mouth;will know where to find it.
                            self.bed_scenario = 30
                            self.toilet_scenario = 32
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 32: # GROSS...;;* key obtained *
                            self.toilet_scenario = 33
                            self.bed_scenario = 34
                            self.key_obtained = True
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 33: # I already got the key...
                            self.visible_speech_balloon = False

                        elif self.speech_balloon_object.scenario == 34: # Drop by anytime pal.
                            self.bed_scenario = 35
                            self.speech_balloon_object.choose_scenario(self, self.reader, self.bed_scenario)

                        elif self.speech_balloon_object.scenario == 35: # Wouldn't count on it "pal" *
                            self.bed_scenario = 34
                            self.visible_speech_balloon = False

    def draw(self):
        # Game loop - draw
        if self.current_screen == 0:
            self.screen.blit(self.start_screen, self.start_screen_rect)
            pygame.display.update()
        elif self.current_screen == 1:
            self.screen.blit(self.instructions_screen, self.instructions_screen_rect)
            pygame.display.update()
        elif self.current_screen == 2:
            self.screen.blit(self.background, self.background_rect)
            self.all_sprites.draw(self.screen)

            if self.visible_speech_balloon == True:
                self.all_sprites.add(self.speech_balloon)
                Text(self, self.highlighted_answer)
            elif self.visible_speech_balloon == False:
                self.all_sprites.remove(self.speech_balloon)

            pygame.display.update()

game = Game()

while game.runs:
    game.new()

def tutorial():
    print("tutorial")

pygame.quit()
