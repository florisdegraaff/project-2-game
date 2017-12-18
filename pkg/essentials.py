import pygame

running = True

def run_essentials(event):

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

        # Skip to next level when 'LCRTL', 'LALT' & 'n' buttons are pressed simultaneously
        if keys[pygame.K_LCTRL] and keys[pygame.K_LALT] and keys[pygame.K_n]:
            return False

    return True

class timer ():

    start_time = None
    timer_length = None

    def __init__ (self, length):
        self.start_time = pygame.time.get_ticks()
        self.timer_length = length * 1000

    def check_timer (self):
        if pygame.time.get_ticks() >= self.start_time + self.timer_length:
            return True
        else:
            return False
