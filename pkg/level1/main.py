from .. import essentials
from .. import display

running = True

def run():
    global running
    while running == True:
        for event in essentials.pygame.event.get():
            running = essentials.run_essentials(event, running, display)

            if event.type == essentials.pygame.KEYDOWN:
                if event.key == essentials.pygame.K_r:
                    print('hello')

        display.update()
