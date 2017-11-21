import pygame

running = True

def run_essentials(event, level, display):

    global pygame
    global running

    # Close the game when the close button on the window is pressed
    if event.type == pygame.QUIT:
        running = False
        return False

    # Input
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        # Close the game when the ESC button is pressed
        if event.key == pygame.K_ESCAPE:
            running = False
            return False

        # Open debug mode when 'LCRTL', 'LALT' & 'k' buttons are pressed simultaneously
        if keys[pygame.K_LCTRL] and keys[pygame.K_LALT] and keys[pygame.K_n]:
            return False

    return True
