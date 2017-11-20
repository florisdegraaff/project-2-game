import pygame

import display
import level_controller

debug = False

running = True
while running:

    screen = display.prepare_screen()

    for event in pygame.event.get():

        # Close the game when the close button on the window is pressed
        if event.type == pygame.QUIT:
            running = False

        # Input
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if event.key == pygame.K_ESCAPE:
                running = False
            if keys[pygame.K_LCTRL] and keys[pygame.K_LALT]:
                if keys[pygame.K_i]:
                    debug = not debug
                if keys[pygame.K_n]:
                    current_level = current_level + 1
                    level_controller.next_level()
    #Output

    #Updates the output to the screen
    display.update(debug)
pygame.quit()
