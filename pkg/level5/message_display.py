import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

pygame = essentials.pygame

black = (0,0,0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text, size, y):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display.window_size[0]/2), y)
    display.window.blit(TextSurf, TextRect)
    pygame.display.update()
