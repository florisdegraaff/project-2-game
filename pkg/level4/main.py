import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

from random import randint

from .Player import Player
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
            running = not timer.check_timer()

        if enemy_spawn_timer.check_timer():
            enemy_spawn_timer = essentials.timer(randint(1,3))
            if randint (0,1) == 0:
                enemies.append(Guard())
            else:
                enemies.append(Bullets())

        # Output
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

        player.update()

        # Update the display to show the changes you made
        display.update()

def tutorial():
    print ("tutorial")
