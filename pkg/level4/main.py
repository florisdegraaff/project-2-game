import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

from random import randint

from .Player import Player, Helicopter
from .Enemy import Guard, Bullets

running = True
pygame = essentials.pygame

def run():
    global running
    global pygame

    jumping = False
    crawling = False

    player = Player ()
    enemies = []

    display.set_title('Level 4')
    timer = essentials.timer(60)
    enemy_spawn_timer = essentials.timer (0)

    while running == True:

        display.prepare_update()

        # Input
        for event in pygame.event.get():
            # Load in the fundemental functions in the game
            running = essentials.run_essentials(event)
            if not running:
                return True

            if event.type == pygame.KEYDOWN:
                if not jumping:
                    if event.key == pygame.K_SPACE:
                        jumping = True
                    elif event.key == pygame.K_LCTRL:
                        crawling = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL:
                    crawling = False
        if running:
            if timer.check_timer():
                helicopter = Helicopter()
                helicopter.update()
                player.end_game()
                if player.position.x > helicopter.position.x:
                    return True
            else:
                if enemy_spawn_timer.check_timer():
                    enemy_spawn_timer = essentials.timer(randint(1,3))
                    if randint (0,1) == 0:
                        enemies.append(Guard())
                    else:
                        enemies.append(Bullets())

        # Output
        pygame.font.init()
        myFont = pygame.font.SysFont('Sans Serif', 48)
        textsurface = myFont.render(str(timer.get_time() / 1000), False, (0, 0, 0))

        pygame.draw.rect(display.window, (0,0,0), pygame.Rect((0, 680), (1280, 40)))

        if crawling:
            player.crawl()
        elif jumping:
            jumping = player.jump()

        for enemy in enemies:
            enemy.update()
            if isinstance (enemy, Guard):
                if player.rect.colliderect(enemy.guard):
                    return False
            else:
                if player.rect.colliderect(enemy.bullet1) or player.rect.colliderect(enemy.bullet2) or player.rect.colliderect(enemy.bullet3):
                    return False

        if not running:
            return True

        display.window.blit(textsurface, (0,0))
        player.update()

        # Update the display to show the changes you made
        display.update()

def tutorial():
    global pygame

    tutorial = True
    while tutorial:

        display.prepare_update()

        # Input
        for event in pygame.event.get():
            # Load in the fundemental functions in the game
            tutorial = essentials.run_essentials(event)
            print (tutorial)
            if not tutorial:
                return False

            if event.type == pygame.KEYDOWN:
                return True

        # Output
        pygame.font.init()
        myFont = pygame.font.SysFont('Sans Serif', 48)

        textsurface1 = myFont.render('Dodge the guards and bullets', False, (0, 0, 0))
        textsurface2 = myFont.render('Press `Space` key to jump', False, (0, 0, 0))
        textsurface3 = myFont.render('Press `Left CTRL` key to crawl', False, (0, 0, 0))
        textsurface4 = myFont.render('Press any key to continue', False, (0, 0, 0))

        display.window.blit(textsurface1, (200,200))
        display.window.blit(textsurface2, (200,230))
        display.window.blit(textsurface3, (200,260))
        display.window.blit(textsurface4, (200,320))
        display.update()
