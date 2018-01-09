from .. import essentials
from .. import display
from .enemy2 import Enemy2
from .enemy import Enemy
from .player import Player
from .floor import Floor
from .sidewall import SideWall
from .topandbottomwall import TopAndBottomWall
from pygame.math import Vector2
from .horizontalwall import HorizontalWall
from .verticalwall import VerticalWall

running = True
pygame = essentials.pygame
2
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

#settings text shown when hit by enemy
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))

def run():
    global running
    global pygame

    screen = pygame.display.set_mode((1280, 720))

    #groups
    playergroup = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    background = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    enemygroup = pygame.sprite.Group()
    #Enemy waypoints
    waypoints = [[x1, y1], [x2, y2], [x3, y3]]
    #Enemy2 waypoints
    waypoints2 = [[1700, 300], [1900, -100], [1500, 300]]
    #player position
    player = Player(((width / 2), (height / 2)))


    #walls
    walltop = TopAndBottomWall(540, -620, all_sprites, walls)
    wallbottom = TopAndBottomWall(540, 410, all_sprites, walls)
    wallleft = SideWall((width / 2) - 100, (height / 2) - 930, all_sprites, walls)
    wallright = SideWall((wallleft.rect.x + (1920 - 50)), (height / 2) - 930, all_sprites, walls)
    wallhorizontal1 = HorizontalWall(700, 200, all_sprites, walls)
    wallvertical1 = VerticalWall(1000, 200, all_sprites, walls)

    #enemy's
    enemy = Enemy((950, -50), waypoints, enemygroup)
    enemy2 = Enemy2((1900, -100), waypoints2, enemygroup)

    #the floor
    floor = Floor(540, -620, background)
    #camera
    camera = Vector2(0, 0)

    display.set_title('Level 2')

    while running:

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #player movement

            elif event.type == pygame.KEYDOWN:
                counter = 0
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

        #update all the groups
        enemygroup.update()
        all_sprites.update()
        playergroup.update()
        background.update()
        walls.update()

        ##player collision with walls
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
        #draw background
        for sprite in background:
            screen.blit(sprite.image, sprite.rect.topleft+camera)
        # draw player and walls
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)
        #draw enemy's
        for sprite in enemygroup:
            screen.blit(sprite.image, sprite.rect.topleft+camera)
        screen.blit(player.image, player.rect.topleft+camera)

        #player collision with enemy
        if pygame.sprite.spritecollide(player, enemygroup, False):
            print("collision")
            screen.blit(textsurface,(600,300))

        #update all the groups
        enemygroup.update()
        all_sprites.update()
        playergroup.update()
        background.update()
        walls.update()

            # Load in the fundemental functions in the game
        running = essentials.run_essentials(event)

        # Output


        # Update the display to show the changes you made
        display.update()
