import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

import time
import random
import os

from .spritesheet import spritesheet
from .message_display import text_objects, message_display

running = True
pygame = essentials.pygame

display_width = display.window_size[0]
display_height = display.window_size[1]

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

W, H = 1280, 800
HW, HH = W / 2, H / 2
AREA = W * H

choepah = spritesheet("files/images/choppah.png", 6, 1)
CENTER_HANDLE = 4
enemy = spritesheet("files/images/enemy.png", 6, 1)
CENTER_HANDLE = 4
background = spritesheet("files/images/background.png", 6, 1)
CENTER_HANDLE = 0
bomb = pygame.image.load('files/images/bomb.png')

def chopper(x,y):
    display.window.blit(choppah,(x,y))

def enemys(enemyx, enemyy, enemyh, enemyw):
    display.window.blit(other_choppah, [enemyx, enemyy, enemyh, enemyw])


def bombs(bombx, bomby, bombh, bombw):
    display.window.blit(bomb, [bombx, bomby, bombh, bombw])

def tutorial():
    background.draw(display.window, index % background.totalCellCount, 0, 0, CENTER_HANDLE)
    message_display("continuously press ARROW_UP to fly upwards", 35, 300)
    time.sleep(3)
    message_display("ARROW_LEFT and ARROW_RIGHT speak for themselves", 35, 400)
    time.sleep(3)

def run():
    global running
    global pygame

    display.set_title("Level 5")

    x = (1500 * 0.1)
    y = (900 * 0.4)
    running = True
    restartGame = False
    ticks = 0
    power_change = 0
    x_change = 0
    y_change = 0
    index = 0

    power = 0
    choppah_width = 245
    choppah_height = 79

    enemy_turbo = 2
    enemy_startx = 1800
    enemy_starty = random.randrange(50, display_height - 50)
    enemy_endy = random.randrange(50, display_height - 50)
    enemy_speed = 7
    enemy_speed += enemy_turbo
    enemy_height = 79
    enemy_width = 245

    bomb_startx = random.randrange(0, display_width)
    bomb_starty = -150
    bomb_speed = -5
    bomb_height = 93
    bomb_width = 25

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('files/sounds/victory.wav'))
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('files/sounds/coptah.wav'))

    while running == True:
        background.draw(display.window, index % background.totalCellCount, 0, 0, CENTER_HANDLE)

        # Input
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    power_change = 0.25
                    power = -5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

        power += power_change
        y += power
        x += x_change
        bomb_starty -= bomb_speed
        enemy_startx -= enemy_speed

        if (ticks > 600 and ticks <= 1200):
            enemy_speed = 12
        if (ticks > 1200):
            enemy_speed = 13
            if y < (bomb_starty) + 93 and (bomb_startx - 0) < x + 93 and bomb_startx + 25 > x:
                if (bomb_starty) < y + 93 and (bomb_startx - 0)< x + 93 and bomb_startx + 25 > x:
                    message_display("bomb", 90, 400)
                    restartGame = True
            bombs(bomb_startx, bomb_starty, bomb_height, bomb_width)
            if bomb_starty > display_height + 100:
                bomb_startx = random.randrange(0, display_width - 100)
                bomb_starty = 0
        if (enemy_starty > y):
            enemy_starty -= 1.2
        if (enemy_starty < y):
            enemy_starty += 1.2

        if enemy_startx < -250:
            enemy_starty = random.randrange(0, display_height - 100)
            enemy_startx = 1500

        choepah.draw(display.window, index % choepah.totalCellCount, x, y, CENTER_HANDLE)
        enemy.draw(display.window, index % enemy.totalCellCount, enemy_startx, enemy_starty, CENTER_HANDLE)

        if x > display_width - 245 or x < -50 or y < 0 or y > display_height:
            return False

        if y < enemy_starty + 79 and (enemy_startx - 150) < x + 79 and (enemy_startx) + 245 > x:
            if enemy_starty < y + 79 and (enemy_startx - 130)< x + 79 and (enemy_startx) + 245 > x:
                return False

        if (ticks == 1200):
            running = False
            message_display("The copts are pissed, brace yourself!", 40, 300)
            pygame.mixer.Channel(0).stop()
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('files/sounds/thestruggle.wav'))
            time.sleep(3)
            running = True

        index += 1
        ticks += 1
        # Update the display to show the changes you made
        display.update()
