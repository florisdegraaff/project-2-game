from .. import essentials
from .. import display

running = True
pygame = essentials.pygame

def run():
    global running
    global pygame

    display.set_title('Level 2')

    while running == True:

        # Input
        for event in pygame.event.get():

            # Load in the fundemental functions in the game
            running = essentials.run_essentials(event)

        # Output


        # Update the display to show the changes you made
        display.update()
