from pkg.foundation import essentials
from pkg.foundation import display

display.prepare_screen()

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
    gameDisplay.blit(levelimg1,(306,300))
    gameDisplay.blit(levelimg2,(480,300))
    gameDisplay.blit(levelimg3,(658,300))
    gameDisplay.blit(levelimg4,(834,300))

    pygame.display.flip()

    lvl1 = pygame.Rect(306,300,140,140)
    lvl2 = pygame.Rect(480,300,140,140)
    lvl3 = pygame.Rect(658,300,140,140)
    lvl4 = pygame.Rect(834,300,140,140)

    while running == True:

        # Input
        for event in pygame.event.get():
            running = essentials.run_essentials(event, False)
            if not running:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos 
                if lvl1.collidepoint(x, y):
                    return 0
                
                if lvl2.collidepoint(x, y):
                    return 1
                
                if lvl3.collidepoint(x, y):
                    return 3
                
                if lvl4.collidepoint(x, y):
                    return 4

        display.update()
