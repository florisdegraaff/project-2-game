import pkg.essentials as essentials

clock = essentials.pygame.time.Clock()
screen = None

def prepare_screen():
    background_color = (122, 122, 122)
    window_size = (1280, 720)

    screen = essentials.pygame.display.set_mode(window_size)
    screen.fill(background_color)

def update():
    essentials.pygame.display.flip()
    clock.tick(15)
    fps = round(clock.get_fps(), 1)
    essentials.pygame.display.set_caption("fps: " + str(fps))
