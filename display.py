import pygame

clock = pygame.time.Clock()

def prepare_screen():
    background_color = (122, 122, 122)
    window_size = (1280, 720)

    screen = pygame.display.set_mode(window_size)
    screen.fill(background_color)

    return screen

def update(debug):
    pygame.display.flip()
    clock.tick(15)
    if debug:
        fps = round(clock.get_fps(), 1)
        pygame.display.set_caption("fps: " + str(fps))
    else:
        pygame.display.set_caption("ESC")
