import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

running = True
pygame = essentials.pygame

def run():
    global running
    global pygame

    display.set_title('Level 1')

    while running == True:

        # Input
        for event in pygame.event.get():

            # Load in the fundemental functions in the game
            running = essentials.run_essentials(event)
            if not running:
                return True

        # Output


        # Update the display to show the changes you made
        display.update()
