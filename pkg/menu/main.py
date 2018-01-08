from .. import essentials
from .. import display
from .. import level_controller
#genieten maar
import pkg.level1.main as level1
import pkg.level2.main as level2
import pkg.level3.main as level3
import pkg.level4.main as level4
import pkg.level5.main as level5


running = True
pygame = essentials.pygame


display_width = 1280
display_height = 720

back = pygame.image.load('files/images/menu.png')
levelimg1 = pygame.image.load('files/images/level1.png').convert()
levelimg2 = pygame.image.load('files/images/level2.png').convert()
levelimg3 = pygame.image.load('files/images/level3.png').convert()
levelimg4 = pygame.image.load('files/images/level4.png').convert()
levelimg5 = pygame.image.load('files/images/level5.png').convert()

gameDisplay = pygame.display.set_mode((display_width, display_height))

def run():
    global running
    global pygame

    display.set_title('Menu')
    gameDisplay.blit(back,(0,0))
    gameDisplay.blit(levelimg1,(236,300))
    gameDisplay.blit(levelimg2,(412,300))
    gameDisplay.blit(levelimg3,(588,300))
    gameDisplay.blit(levelimg4,(764,300))
    gameDisplay.blit(levelimg5,(940,300))
    
    pygame.display.flip()
    
    lvl1 = pygame.Rect(236,300,140,140)
    lvl2 = pygame.Rect(412,300,140,140)
    lvl3 = pygame.Rect(588,300,140,140)
    lvl4 = pygame.Rect(764,300,140,140)
    lvl5 = pygame.Rect(940,300,140,140)

    while running == True:

        # Input
        for event in pygame.event.get():
            running = essentials.run_essentials(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if lvl1.collidepoint(x, y):
                    level1.run()
                if lvl2.collidepoint(x, y):
                    level2.run()
                if lvl3.collidepoint(x, y):
                    level3.run()
                if lvl4.collidepoint(x, y):
                    level4.run()
                if lvl5.collidepoint(x, y):
                    level5.run()

        display.update()