from .. import essentials
from .. import display

from .Player import Player

running = True
pygame = essentials.pygame

def run():
    global running
    global pygame

    jumping = False
    crawling = False

    player = Player ()

    display.set_title('Level 4')
    timer = essentials.timer(60)

    while running == True:

        display.prepare_update()

        # Input
        for event in pygame.event.get():
            # Load in the fundemental functions in the game
            running = essentials.run_essentials(event)

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


        # Output
        pygame.draw.rect(display.window, (0,0,0), pygame.Rect((0, 680), (1280, 40)))

        if crawling:
            player.crawl()
        elif jumping:
            jumping = player.jump()

        player.update()

        # Update the display to show the changes you made
        display.update()
