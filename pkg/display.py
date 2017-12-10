import pkg.essentials as essentials

clock = essentials.pygame.time.Clock()
window_size = (1280, 720)
background_color = (122, 122, 122)
screenTitle = ""

def prepare_screen():
    global window_size
    global background_color

    screen = essentials.pygame.display.set_mode(window_size)
    screen.fill(background_color)

def update():
    global clock

    essentials.pygame.display.flip()
    clock.tick(30)
    fps = round(clock.get_fps(), 1)
    essentials.pygame.display.set_caption("fps: " + str(fps) + " - " + screenTitle)

def set_background(red, green, blue):
    global background_color

    if red > 255 or green > 255 or blue > 255 or red < 0 or green < 0 or blue < 0:
        print('Background requires rgb values between 0 and 255')
        return
    background_color = (red, green, blue)

def set_title (title):
    if not (type(title) is str):
        print('`title` variable requires a type of `string`')
        return
    global screenTitle
    screenTitle = title
