import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

# Mini Game 1
import pygame
import random
import csv

from .sprites import *
from .settings import *
from os import path

running = True
pygame = essentials.pygame

all_sprites = None
player = None
walls = None
bed = None
bars = None
jaildoor = None
toilet = None
exits = None
background = None
background_rect = None
speech_balloon_object = None
jailDoor = None

interaction_mark1 = None
interaction_mark2 = None
interaction_mark3 = None
interaction_mark4 = None
key_obtained = None

bed_scenario = None
toilet_scenario = None
mob_scenario = None

reader = None

visible_speech_balloon = False

def run ():
    global running
    global pygame

    global visible_speech_balloon
    global speech_balloon
    global interaction_mark1
    global interaction_mark2
    global interaction_mark3
    global interaction_mark4
    global key_obtained

    global bed_scenario
    global toilet_scenario
    global mob_scenario

    display.set_title('Level 1')

    new()
    load_data()

    while running:
        display.prepare_update()

    # Input
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if not running:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if visible_speech_balloon:
                        if multiple_choice_answers:
                            if highlighted_answer > highlighted_answer_minimum_boundary:
                                highlighted_answer -= 1
                if event.key == pygame.K_DOWN:
                    if visible_speech_balloon:
                        if multiple_choice_answers:
                            if highlighted_answer < highlighted_answer_maximum_boundary:
                                highlighted_answer += 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if visible_speech_balloon:
                        if speech_balloon_object.scenario == 1: # I don't have to go...
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 2 and highlighted_answer == 4: # Do you want to play a game?;Answer 3 questions...;and I'll hand over the key --> Yes
                            bed_scenario = 3
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 2 and highlighted_answer == 5: # Do you want to play a game?;Answer 3 questions...;and I'll hand over the key --> No
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 3: # Here is my first question:;The person who knows he uses;it, doesn't know he uses it.;What is it?
                            bed_scenario = 4
                            multiple_choice_answers = True
                            highlighted_answer = 1
                            highlighted_answer_minimum_boundary = 1
                            highlighted_answer_maximum_boundary = 4
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 4 and highlighted_answer != 4: # Insurance;Necktie;Sugar;Coffin
                            bed_scenario = 5
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 4 and highlighted_answer == 4: # Insurance;Necktie;Sugar;Coffin
                            bed_scenario = 6
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 5: # WRONG!;Get used to being here,;cause you're going to be;here for a while...
                            bed_scenario = 3
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 6: # That's correct.;Here's my next question:
                            bed_scenario = 7
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 7: # Have you ever heard of a;dyslexic Satanist?
                            bed_scenario = 8
                            multiple_choice_answers = True
                            highlighted_answer = 1
                            highlighted_answer_minimum_boundary = 1
                            highlighted_answer_maximum_boundary = 4
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 8 and highlighted_answer != 2: # They prey to Christ;He sold his soul to Santa;There are none;No
                            bed_scenario = 9
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 8 and highlighted_answer == 2: # They prey to Christ;He sold his soul to Santa;There are none;No
                            bed_scenario = 10
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 9: # You're wrong!;I guess you're not so smart;...
                            bed_scenario = 7
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 10: #  Okay. For my final game,;I want you to insult the;other inmate's mother.
                            bed_scenario = 11
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 11: # We're gonna torture him;with the infamous your momma jokes.
                            bed_scenario = 12
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 12: # Unfortunately for you,;I only know the setups,;you're gonna have to come;up with the punchlines
                            bed_scenario = 13
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 13: # Go talk to the other inmate.
                            bed_scenario = 10
                            mob_scenario = 15
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 14: # Go away.;I have nothing to say.
                            mob_scenario = 14
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 15: # Okay, here goes nothing... *
                            mob_scenario = 16
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 16: # HEY YOU!;YO' MOMMA'S SO FAT...
                            mob_scenario = 17
                            multiple_choice_answers = True
                            highlighted_answer = 1
                            highlighted_answer_minimum_boundary = 1
                            highlighted_answer_maximum_boundary = 3
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 17 and highlighted_answer != 2: # ...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...SHE HAS MORE FOLDS,;THAN AN ORIGAMI ACCORDEON!;...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!
                            mob_scenario = 18
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 17 and highlighted_answer == 2: # ...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...SHE HAS MORE FOLDS,;THAN AN ORIGAMI ACCORDEON!;...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!
                            mob_scenario = 19
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 18: # Stop talking trash!;You suck at this!
                            mob_scenario = 15
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 19: # Not a word about my mother!;She's a saint.
                            mob_scenario = 20
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 20: # YO' MOMMA'S SO RADIANT...
                            mob_scenario = 21
                            multiple_choice_answers = True
                            highlighted_answer = 1
                            highlighted_answer_minimum_boundary = 1
                            highlighted_answer_maximum_boundary = 3
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 21 and highlighted_answer != 1: # ...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!;...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!
                            mob_scenario = 22
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 21 and highlighted_answer == 1: # ...IF SHE FELL IN NUCLEAR WASTE,;NO ONE WOULD NOTICE!;...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!
                            mob_scenario = 23
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 22: # You ain't hurtin nobody,;you little bitch!
                            mob_scenario = 15
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 23: # Ahhh, it hurts...;IT HURTS!
                            mob_scenario = 24
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 24: # YO' MOMMA'S SO PUNCTUAL...
                            mob_scenario = 25
                            multiple_choice_answers = True
                            highlighted_answer = 1
                            highlighted_answer_minimum_boundary = 1
                            highlighted_answer_maximum_boundary = 3
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 25 and highlighted_answer != 2: # ...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...THE ONLY TIME SHE'S LOW;IS AT A LIMBO CONTEST!
                            mob_scenario = 26
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 25 and highlighted_answer == 2: # ...SHE BRINGS COUPONS TO;THE PENNY ARCADE!;...SHE SHOWED UP EARLY;FOR HER OWN FUNERAL!;...THE ONLY TIME SHE'S LOW;IS AT A LIMBO CONTEST!
                            mob_scenario = 27
                            multiple_choice_answers = False
                            highlighted_answer = 0
                            speech_balloon_object.choose_scenario(self, reader, mob_scenario)

                        elif speech_balloon_object.scenario == 26: # You had your chance,;now FUCK OFF!
                            mob_scenario = 15
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 27: # Enough, enough!; I'm suffocating...;sob.. sob... *
                            mob_scenario = 28
                            bed_scenario = 30
                            speech_balloon_object.choose_scenario(self, reader, 29)

                        elif speech_balloon_object.scenario == 28: # I'm done talking to you;Leave me alone...
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 29: # Now to claim the key;and get the fuck outta here! *
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 30: # Man...;I had the time of my life!!;Didn't know you had it in ya!
                            bed_scenario = 31
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 31: # Unfortunately for you,;I don't have the key on me,;but I'm sure that you little;POTTY mouth;will know where to find it.
                            bed_scenario = 30
                            toilet_scenario = 32
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 32: # GROSS...;;* key obtained *
                            toilet_scenario = 33
                            bed_scenario = 34
                            key_obtained = True
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 33: # I already got the key...
                            visible_speech_balloon = False

                        elif speech_balloon_object.scenario == 34: # Drop by anytime pal.
                            bed_scenario = 35
                            speech_balloon_object.choose_scenario(self, reader, bed_scenario)

                        elif speech_balloon_object.scenario == 35: # Wouldn't count on it "pal" *
                            bed_scenario = 34
                            visible_speech_balloon = False

    # Output
        pygame.mixer.init()
        pygame.font.init()
        font = pygame.font.Font(FONT, 19)
        font2 = pygame.font.Font(FONT, 13)

        all_sprites.update()

        if player.speedx or player.speedy > 0:
            all_sprites.remove(interaction_mark1, interaction_mark2, interaction_mark3, interaction_mark4)
            all_sprites.remove(speech_balloon)

        # for interaction with the bed "object"
        if player.rect.x >= 930 and player.rect.y <= 222:

            if player.keys[pygame.K_SPACE]:
                if bed_scenario == 2:
                    multiple_choice_answers = True
                    highlighted_answer = 4
                    highlighted_answer_minimum_boundary = 4
                    highlighted_answer_maximum_boundary = 5
                speech_balloon_object.choose_scenario(visible_speech_balloon, reader, bed_scenario)

        # for interaction with the toilet
        if (player.rect.x >= 640 and player.rect.x <= 772) and player.rect.y <= 150:
            if player.keys[pygame.K_SPACE]:

                speech_balloon_object.choose_scenario(visible_speech_balloon, reader, toilet_scenario)

        # for interaction with the bars of the player's cell
        if player.rect.x == 622:
            if player.keys[pygame.K_SPACE]:
                if key_obtained == True:
                    all_sprites.remove(bars)
                    bars.remove(jailDoor)
                elif key_obtained == False:
                    speech_balloon_object.choose_scenario(visible_speech_balloon, reader, mob_scenario)


        hits_wall = pygame.sprite.spritecollide(player, walls, False)
        if hits_wall:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy

        hits_bed = pygame.sprite.spritecollide(player, bed, False)
        if hits_bed:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy

            if player.speedx == 0:
                all_sprites.add(interaction_mark2)


            if player.speedy == 0:
                all_sprites.add(interaction_mark2)



        hits_bars = pygame.sprite.spritecollide(player, bars, False)
        if hits_bars:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy

            if key_obtained == False:


                if player.speedx == 0:
                    all_sprites.add(interaction_mark1)

                if player.speedy == 0:
                    all_sprites.add(interaction_mark1)
                    if player.keys[pygame.K_SPACE]:
                        #key_obtained = False

            if key_obtained == True:
                all_sprites.remove(bars)
                bars.remove(jailDoor)

        hits_jaildoor = pygame.sprite.spritecollide(player, jaildoor, False)
        if hits_jaildoor:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy


        hits_toilet = pygame.sprite.spritecollide(player, toilet, False)
        if hits_toilet:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy
            if player.speedx == 0:
                all_sprites.add(interaction_mark3)


            if player.speedy == 0:
                all_sprites.add(interaction_mark3)


        hits_exit = pygame.sprite.spritecollide(player, exits, False)
        if hits_exit:
            player.rect.x = player.rect.x - player.speedx
            player.rect.y = player.rect.y - player.speedy
            return True

        display.window.blit(background, background_rect)
        all_sprites.draw(display.window)

        if visible_speech_balloon:
            all_sprites.add(speech_balloon)
            Text(speech_balloon_object, font, reader, highlighted_answer)
        else:
            all_sprites.remove(speech_balloon)
        pygame.display.update()

def tutorial():
    global pygame

    tutorial = True
    instruction = pygame.image.load("pkg/level1/images/instructions_screen.jpg")
    while tutorial:

        display.prepare_update()

        # Input
        for event in pygame.event.get():
            # Load in the fundemental functions in the game
            tutorial = essentials.run_essentials(event)
            if not tutorial:
                return False

            if event.type == pygame.KEYDOWN:
                return True

        # Output
        display.window.blit(instruction, (0,0))
        display.update()

def load_data():
    global background
    global background_rect
    global reader

    dir = path.dirname(__file__)
    image_dir = path.join(dir, 'images')
    script_dir = path.join(dir, 'scripts')
    music_dir = path.join(dir, 'music')

    # load spritesheet image
    spritesheet = Spritesheet(path.join(image_dir, SPRITESHEET))

    # load game background
    background = pygame.image.load(path.join(image_dir, BACKGROUND)).convert()
    background_rect = background.get_rect()

    # load music
    pygame.mixer.music.load(MUSIC)
    pygame.mixer.music.play(-1, 0.0)

    # load script
    with open(path.join(script_dir, SCRIPT)) as csv_file:
        reader = list(csv.reader(csv_file, delimiter = ';'))
        total_rows = len(reader)

def new():
    # start a new game
    global all_sprites
    global player
    global walls
    global bed
    global bars
    global jaildoor
    global toilet
    global exits
    global speech_balloon_object
    global jailDoor

    global visible_speech_balloon
    global speech_balloon
    global interaction_mark1
    global interaction_mark2
    global interaction_mark3
    global interaction_mark4
    global key_obtained

    global bed_scenario
    global toilet_scenario
    global mob_scenario

    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    bed = pygame.sprite.Group()
    bars = pygame.sprite.Group()
    exits = pygame.sprite.Group()
    jaildoor = pygame.sprite.Group()
    interaction_mark = pygame.sprite.Group()
    toilet = pygame.sprite.Group()
    player = Player(visible_speech_balloon)
    mob = pygame.sprite.Group()
    speech_balloon = pygame.sprite.Group()
    text = pygame.sprite.Group()
    all_sprites.add(player, walls, bed, bars, jaildoor, exits, interaction_mark, toilet, mob, speech_balloon, text)
    visible_speech_balloon = False
    multiple_choice_answers = False
    highlighted_answer = 0
    highlighted_answer_minimum_boundary = 0
    highlighted_answer_maximum_boundary = 0
    remove_textbox = False
    key_obtained = True
    toilet_scenario = 1
    bed_scenario = 2
    mob_scenario = 14
    start_screen_visible = True

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
    jailDoor = Jaildoor()
    # the guy in the other cell
    mob1 = Mob(130, 360)
    # the toilet in the player's cell
    toilet1 = Toilet(700, 50)
    # the toilet in the other cell
    toilet2 = Toilet(70, 50)
    # the interaction mark for the bars in the player's cell
    interaction_mark1 = InteractionMark(150, 300, 8, 8)
    # the interaction mark for the bed "object" in the player's cell
    interaction_mark2= InteractionMark(960, 5, 8, 8)
    # the interaction mark for the toilet
    interaction_mark3= InteractionMark(700, 5, 8, 8)
    # the interaction mark for the unlocked door
    interaction_mark4= InteractionMark(575, 280, 8, 8)
    # the speech balloon
    speech_balloon_object = SpeechBalloon(300, 490, 300, 300)

    all_sprites.add(wall1, wall2, wall3, wall4, bedObject, barsObjectUp, barsObjectDown, jailDoor, exitUp, exitDown, toilet1, toilet2, mob1)
    walls.add(wall1, wall2, wall3, wall4)
    exits.add(exitUp, exitDown)
    bed.add(bedObject)
    bars.add(barsObjectUp, barsObjectDown, jailDoor)
    toilet.add(toilet1, toilet2)
    speech_balloon.add(speech_balloon_object)
