from .. import essentials
from .. import display

running = True
pygame = essentials.pygame

def run():
    global running
    global pygame

    jumping = False
    crawling = False
    jumptimer = -10

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
            player_size = (100, 100)
            player_pos = (100, 580)
        elif jumping:
            player_size = (100, 200)
            player_pos = (100, 80 + (jumptimer * jumptimer) * 4)
            jumptimer += 1
            if jumptimer > 10:
                jumping = False
                jumptimer = -10
        else:
            player_size = (100, 200)
            player_pos = (100, 480)

        pygame.draw.rect(display.window, (0,0,0), pygame.Rect(player_pos, player_size))

        # Update the display to show the changes you made
        display.update()
