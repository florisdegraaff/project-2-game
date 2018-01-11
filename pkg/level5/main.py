import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

import time
import random
import os

from .spritesheet import spritesheet
from .message_display import text_objects, message_display

running = True
pygame = essentials.pygame

#get display width and height from display controller
display_width = display.window_size[0]
display_height = display.window_size[1]

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

choepah = spritesheet("files/images/choppah.png", 6, 1)
CENTER_HANDLE = 4
enemy = spritesheet("files/images/enemy.png", 6, 1)
CENTER_HANDLE = 4
background = spritesheet("files/images/background.png", 6, 1)
CENTER_HANDLE = 0
bomb = pygame.image.load('files/images/bomb.png')

def bombs(bombx, bomby, bombh, bombw):
    display.window.blit(bomb, [bombx, bomby, bombh, bombw])

def lose(cause):
    msg = "Hit " + cause
    message_display(msg, 35, 300)
    time.sleep(2)
    
def tutorial():
    background.draw(display.window, 1 % background.totalCellCount, 0, 0, CENTER_HANDLE)
    message_display("continuously press ARROW_UP to fly upwards", 35, 200)
    time.sleep(1)
    message_display("Press ARROW_LEFT/ARROW_RIGHT to fly left/right", 35, 300)
    time.sleep(1)
    message_display("Dont hit a copter or bomb and survive for one minute to escape", 35, 400)
    time.sleep(1)

def run():
    global running
    global pygame
    #set title for current level
    display.set_title("Level 5")

    #player configuration
    x, y = (1500 * 0.1),(900 * 0.4)
    choppah_width = 245
    choppah_height = 79
    power = 0
    power_change = 0
    x_change = 0
    y_change = 0
    
    #enemy copter configuration
    enemy_turbo = 2
    enemy_startx = 1800
    enemy_starty = random.randrange(50, display_height - 50)
    enemy_endy = random.randrange(50, display_height - 50)
    enemy_speed = 7
    enemy_speed += enemy_turbo
    enemy_height = 79
    enemy_width = 245

    #bomb configuration
    bomb_startx = random.randrange(0, display_width)
    bomb_starty = -150
    bomb_speed = -5
    bomb_height = 93
    bomb_width = 25

    #other values
    running = True
    gameWon = False
    ticks = 0
    index = 0

    #music/sounds (optional)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('files/sounds/victory.wav'))
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('files/sounds/coptah.wav'))

    #game loop
    while running == True:
        
        #catch all pressed keys
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if event.type == pygame.QUIT:
                running = False

            #direction change based on pressed key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    power_change = 0.25
                    power = -5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    
        #set the new position based on direction change
        power += power_change
        #player y pos remains same, x pos goes forward on game win
        if (ticks > 200):
            power = 0
            x_change = 5
        y += power
        x += x_change
        bomb_starty -= bomb_speed
        enemy_startx -= enemy_speed
            
        if (bomb_starty > display_height + 100):
            bomb_startx = random.randrange(0, display_width - 100)
            bomb_starty = 0
        if (enemy_starty > y):
            enemy_starty -= 1.2
        if (enemy_starty < y):
            enemy_starty += 1.2
        
        if enemy_startx < -250:
            enemy_starty = random.randrange(0, display_height - 100)
            enemy_startx = 1500

            
        #drawing rectangles for entities with collision
        bombRect = pygame.draw.rect(display.window, (0,0,0), (bomb_startx,bomb_starty,bomb_width,bomb_height))
        choepahRect = pygame.draw.rect(display.window, (0,0,0), (x,y,choppah_width,choppah_height))
        enemyRect = pygame.draw.rect(display.window, (0,0,0), (enemy_startx,enemy_starty,enemy_width,enemy_height))
        
        #draw the background over the rectangles
        background.draw(display.window, index % background.totalCellCount, 0, 0, CENTER_HANDLE)
        
        #draw sprites/images on the position of the rectangles
        choepah.draw(display.window, index % choepah.totalCellCount, x, y, CENTER_HANDLE)
        enemy.draw(display.window, index % enemy.totalCellCount, enemy_startx, enemy_starty, CENTER_HANDLE)
            
        #after 20 seconds enemy copters speedup
        if (ticks > 1200 and ticks <= 2400):
            enemy_speed = 12

        #after 40 seconds 
        if (ticks > 2400):
            enemy_speed = 13
            #when player collides with bomb, restart level
            bombs(bomb_startx, bomb_starty, bomb_height, bomb_width)
            if choepahRect.colliderect(bombRect):
                lose("by bomb")
                return False
        #display message after 40 seconds
        if (ticks == 2400):
            running = False
            message_display("The copts are pissed!", 40, 300)
            #pygame.mixer.Channel(0).stop()
            #pygame.mixer.Channel(2).play(pygame.mixer.Sound('files/sounds/thestruggle.wav'))
            time.sleep(3)
            running = True

        #game win
        if (ticks > 200):
            enemy_starty = 1100
            bomb_starx = 2000
            gameWon = True
            if (x > 1280):
                message_display("You have escaped!", 35, 350)
                if (x > 2500):
                    gameWon = True
                    return True
                
                   
        #when a player collides with border, restart level
        if (x > display_width - choppah_width or x < 0 or y < 0 or y+choppah_height > display_height) and not gameWon:
            lose("the border")
            return False
        
        #when player collides with enemy copter, restart level
        if choepahRect.colliderect(enemyRect):
            lose("by copter")
            return False

        index += 1
        ticks += 1

        #Makes the changes visible
        display.update()
