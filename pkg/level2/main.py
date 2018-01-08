from .. import essentials
from .. import display
from pygame.math import Vector2
from enemy import *
from floor import *
from player import *
from sidewall import *
from topandbottomwall import *
running = True
pygame = essentials.pygame

width = 1280
height = 720
x1 = 850
y1 = 150
x2 = 950
y2 = -50
x3 = 1100
y3 = 150
x = 0
y = 0

def run():
    global running
    global pygame
    
    playergroup = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    #Enemy waypoints
    waypoints = [[x1, y1], [x2, y2], [x3, y3]]
    #the floor
    floor = Floor(540, -620, all_sprites)
    
    player = Player(((width / 2), (height / 2)))

    walls = pygame.sprite.Group()

    walltop = TopAndBottomWall(540, -620, all_sprites, walls)
    wallbottom = TopAndBottomWall(540, 410, all_sprites, walls)
    wallleft = SideWall((width / 2) - 100, (height / 2) - 930, all_sprites, walls)
    wallright = SideWall((wallleft.rect.x + (1920 - 50)), (height / 2) - 930, all_sprites, walls)

    enemy = Enemy((950, -50), waypoints, all_sprites)

    camera = Vector2(0, 0)
    
    display.set_title('Level 2')
    
    while running:


        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #player movement    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.vel.x = 5
                    player.vel.y = 0
                elif event.key == pygame.K_a:
                    player.vel.x = -5
                    player.vel.y = 0
                elif event.key == pygame.K_w:
                    player.vel.y = -5
                    player.vel.x = 0
                elif event.key == pygame.K_s:
                    player.vel.y = 5
                    player.vel.x = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d and player.vel.x > 0:
                    player.vel.x = 0
                    player.vel.y = 0
                elif event.key == pygame.K_a and player.vel.x < 0:
                    player.vel.x = 0
                    player.vel.y = 0
                elif event.key == pygame.K_w:
                    player.vel.y = 0
                    player.vel.x = 0
                elif event.key == pygame.K_s:
                    player.vel.y = 0
                    player.vel.x = 0


        all_sprites.update()

        # move player horizontal
        player.rect.x += player.vel.x
        # check collision horizontal
        if pygame.sprite.spritecollide(player, walls, False):
            # move it back
            player.rect.x -= player.vel.x
            # reset speed
            player.vel.x = 0

        # move player vertical
        player.rect.y += player.vel.y
        # check collision vertical
        if pygame.sprite.spritecollide(player, walls, False):
            # move it back
            player.rect.y -= player.vel.y
            # reset speed
            player.vel.y = 0

        camera -= player.vel

        screen.fill((0, 0, 0))
        
        #print(player.rect)

        # draw player
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)
            
        screen.blit(player.image, player.rect.topleft+camera)
        

            # Load in the fundemental functions in the game
        running = essentials.run_essentials(event)

        # Output


        # Update the display to show the changes you made
        display.update()
