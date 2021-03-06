import pkg.foundation.display as display
import pkg.foundation.essentials as essentials
from .enemy import Enemy
from .enemy2 import Enemy2
from .enemy3 import Enemy3
from .enemy4 import Enemy4
from .player import Player
from .floor import Floor
from .sidewall import SideWall
from .topandbottomwall import TopAndBottomWall
from pygame.math import Vector2
from .horizontalwall import HorizontalWall
from .verticalwall import VerticalWall
import time
from itertools import cycle
from .tafel import Tafel
from .message_display import *
import pygame.mixer

running = True
pygame = essentials.pygame
width = 1280
height = 720
x1 = 850
y1 = 150
x2 = 950
y2 = -50
x3 = 1100
y3 = 150
x = 0
y = 0
#chopper image
gettothechopper = pygame.image.load("pkg/level2/images/gettothechopper.png").convert_alpha()

#arnold image
busted = pygame.image.load("pkg/level2/images/busted.png").convert_alpha()

def tutorial():
    global pygame
    display.window.fill((107, 115, 122))
    message_display("Find the phone to connect Arnold.", 30, 200, 600)
    message_display("Dont let the guards get you.", 30, 230, 600)
    message_display("Press WASD-Keys to move", 30, 260, 600)
    message_display("Press any key to continue", 30, 320, 600)
    while True:
        #End tutorial when any keys is pressed
        for event in pygame.event.get():
            # Load in fundemental functions in the game
            tutorial = essentials.run_essentials(event)
            if not tutorial:
                return False

            if event.type == pygame.KEYDOWN:
                return True

def run():
    global running
    global pygame

    #while running play the music
    pygame.mixer.init(44100, -16,2,2048)
    pygame.mixer.music.load("pkg/level2/sounds/elevator.mp3")
    pygame.mixer.music.play(-1)

    timer = essentials.timer(3)

    #groups
    playergroup = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    background = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    levelwalls = pygame.sprite.Group()
    enemygroup = pygame.sprite.Group()
    tafelgroup = pygame.sprite.Group()

    #Enemy waypoints
    waypoints = [[620, 100], [735, -455], [1890, -550], [1890, -450], [615, -545]]
    #Enemy2 waypoints
    waypoints2 = [[1130, 165],[1115, 315], [1135, -210], [1680, -210], [1680, 165]]
    #Enemy3 waypoints
    waypoints3 = [[2175, 290], [1300, 350], [1300, 290], [2175, 350]]
    #Enemy4 waypoints
    waypoints4 = [[1800, 0],[1975, -125], [2300, -130], [2300, 120], [1970, 120]]
    #player position
    player = Player(((width / 2), (height / 2)))

    #side, top and bottom walls
    walltop = TopAndBottomWall(540, -620, all_sprites, walls)
    wallbottom = TopAndBottomWall(540, 410, all_sprites, walls)
    wallleft = SideWall((width / 2) - 100, (height / 2) - 930, all_sprites, walls)
    wallright = SideWall((wallleft.rect.x + (1920 - 50)), (height / 2) - 930, all_sprites, walls)

    ##horizontal and vertical walls
    #three in the beginning of the level
    wallvertical1 = VerticalWall(740, 230, levelwalls, walls)
    wallhorizontal1 = HorizontalWall(740, 180, levelwalls, walls)
    wallvertical2 = VerticalWall(940, 30, levelwalls, walls)

    #top part of the level
    wallvertical3 = VerticalWall(790, -370, levelwalls, walls)
    wallhorizontal2 = HorizontalWall(840, -370, levelwalls, walls)
    wallhorizontal3 = HorizontalWall(1040, -370, levelwalls, walls)
    wallhorizontal4 = HorizontalWall(1240, -370, levelwalls, walls)
    wallhorizontal5 = HorizontalWall(1440, -370, levelwalls, walls)
    wallhorizontal6 = HorizontalWall(1640, -370, levelwalls, walls)
    wallvertical3 = VerticalWall(1840, -370, levelwalls, walls)
    wallvertical4 = VerticalWall(2140, -370, levelwalls, walls)

    #bottom part of the level
    wallvertical5 = VerticalWall(1190, 230, levelwalls, walls)
    wallhorizontal7 = HorizontalWall(1690, 230, levelwalls, walls)
    wallhorizontal8 = HorizontalWall(2240, 230, levelwalls, walls)

    #big block in the middle
    wallhorizontal9 = HorizontalWall(1340, -70, levelwalls, walls)
    wallhorizontal10 = HorizontalWall(1340, -20, levelwalls, walls)
    wallhorizontal11 = HorizontalWall(1340, 30, levelwalls, walls)
    wallhorizontal12 = HorizontalWall(1340, 80, levelwalls, walls)

    #small block in the middle
    wallhorizontal13 = HorizontalWall(2040, -20, levelwalls, walls)
    wallhorizontal14 = HorizontalWall(2040, 30, levelwalls, walls)

    #enemy's
    enemy = Enemy((620, 50), waypoints, enemygroup)
    enemy2 = Enemy2((1115, 315), waypoints2, enemygroup)
    enemy3 = Enemy3((1900, -100), waypoints3, enemygroup)
    enemy4 = Enemy4((1900, -100), waypoints4, enemygroup)

    #the floor
    floor = Floor(540, -620, background)

    #tafel
    tafel = Tafel(2300, 300, tafelgroup)

    #camera
    camera = Vector2(0, 0)

    display.set_title('Level 2')

    #animated sprite
    clock = pygame.time.Clock()
    dt = clock.tick(60)

    while running:
        # Input
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if not running:
                return True
            #player movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.vel.x = 5
                    player.vel.y = 0
                elif event.key == pygame.K_a:
                    player.vel.x = -5
                    player.vel.y = 0
                elif event.key == pygame.K_w:
                    player.vel.y = -5
                    player.vel.x = 0
                elif event.key == pygame.K_s:
                    player.vel.y = 5
                    player.vel.x = 0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d and player.vel.x > 0:
                    player.vel.x = 0
                elif event.key == pygame.K_a and player.vel.x < 0:
                    player.vel.x = 0
                elif event.key == pygame.K_w:
                    player.vel.y = 0
                elif event.key == pygame.K_s:
                    player.vel.y = 0

        #update all the groups
        enemygroup.update()
        all_sprites.update()
        playergroup.update()
        background.update()
        walls.update()
        tafelgroup.update()

        ##player collision with walls
        # move player horizontal
        player.rect.x += player.vel.x
        # check collision horizontal
        if pygame.sprite.spritecollide(player, walls, False):
            # move it back
            player.rect.x -= player.vel.x
            # reset speed
            player.vel.x = 0

        # move player vertical
        player.rect.y += player.vel.y
        # check collision vertical
        if pygame.sprite.spritecollide(player, walls, False):
            # move it back
            player.rect.y -= player.vel.y
            # reset speed
            player.vel.y = 0

        camera -= player.vel

        display.window.fill((0, 0, 0))

        #draw background
        for sprite in background:
            display.window.blit(sprite.image, sprite.rect.topleft+camera)
        #draw walls in level
        for sprite in levelwalls:
            display.window.blit(sprite.image, sprite.rect.topleft+camera)
        # draw player and walls
        for sprite in all_sprites:
            display.window.blit(sprite.image, sprite.rect.topleft+camera)
        #draw enemy's
        for sprite in enemygroup:
            display.window.blit(sprite.image, sprite.rect.topleft+camera)

        #draw tafel
        for sprite in tafelgroup:
            display.window.blit(sprite.image, sprite.rect.topleft+camera)
        #draw player
        display.window.blit(player.image, player.rect.topleft+camera)

        #update all the groups
        all_sprites.update()
        playergroup.update()
        background.update()
        walls.update()
        tafelgroup.update()

        # collision with enemy
        if pygame.sprite.spritecollide(player, enemygroup, False):
            #show busted
            display.window.blit(busted, [400, 150])
            #load hasta la vista
            hastalavista = pygame.mixer.music.load("pkg/level2/sounds/hastalavista.mp3")
            #play arnold sound
            pygame.mixer.music.play(0)
            display.update()
            time.sleep(3)
            return False

        #collision with table
        if pygame.sprite.spritecollide(player, tafelgroup, False):
            #show arnold face
            display.window.blit(gettothechopper, [0, 0])
            #load arnold chopper sound
            pygame.mixer.music.load("pkg/level2/sounds/gettothechopper.mp3")
            #play arnold chopper sound
            pygame.mixer.music.play(0)
            display.update()
            time.sleep(6)
            return True


            # Load in the fundemental functions in the game

        # Output

        ## Update the display to show the changes you made
        # counter for player animation
        player.counter(dt)
        player.counter2(dt)
        player.counter3(dt)
        player.counter4(dt)

        ##counter for enemy animation
        enemy.counter(dt)
        enemy2.counter(dt)
        enemy3.counter(dt)
        enemy4.counter(dt)
        enemygroup.update()

        display.update()
