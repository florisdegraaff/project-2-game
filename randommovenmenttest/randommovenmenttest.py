import pygame
import random
import os
import time
from random import choices
from random import randint

pygame.init()
a = 0
b = 0
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
done = False
n = 0
x = 0
y = 0
x_wall = 0
y_wall = 0
clock = pygame.time.Clock()
WHITE = (255,255,255)
RED = (255,0,0)
change_x = 0
change_y = 0

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load("character.png") 
      self.rect = self.image.get_rect()
      self.rect.x = width / 2
      self.rect.y = height / 2

    #player movement
    def update(self):
      self.vx = x
      self.vy = y
      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT]:
        self.vx = -5
        self.vy = 0
      elif key[pygame.K_RIGHT]:
        self.vx = 5
        self.vy = 0
      if key[pygame.K_UP]:
        self.vy = -5
        self.vx = 0
      elif key[pygame.K_DOWN]:
        self.vy = 5
        self.vx = 0
      self.rect.x = self.rect.x + self.vx
      self.rect.y = self.rect.y + self.vy

#enemy class
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("enemy.png")
    self.image = pygame.transform.scale(self.image, (int(50), int(50)))
    self.rect = self.image.get_rect()
    self.rect.x = width / 3
    self.rect.y = height / 3
    self.speedy = random.randrange(-5, 5)
    self.speedx = random.randrange(-5, 5)

  def update(self):
    self.rect.x += self.speedx
    self.rect.y += self.speedy

#wall class
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("wall.png") 
    self.image = pygame.transform.scale(self.image, (int(50), int(50)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

#player sprite group
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

#enemy sprite group
enemys = pygame.sprite.Group()
enemy = Enemy()
enemy2 = Enemy()
enemys.add(enemy, enemy2)

#all the wall sprites
wall_list = pygame.sprite.Group()
wall = Wall(x_wall, y_wall)
wall2 = Wall((x_wall + 50), y_wall)
wall3 = Wall((x_wall + 100), y_wall)
wall4 = Wall((x_wall + 150), y_wall)
wall5 = Wall((x_wall + 200), y_wall)
wall6 = Wall((x_wall + 250), y_wall)


#add all the walls to the list to draw them later
wall_list.add(wall, wall2, wall3, wall4, wall5, wall6)

#add all the walls here to fix the collision
all_walls = (wall, wall2, wall3, wall4, wall5, wall6)

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    sprites.update()
    wall_list.update()
    enemys.update()



    #player can't go off screen
    if player.rect.bottom > screen.get_rect().bottom:
      player.rect.y = player.rect.y - player.vy

    if player.rect.top < screen.get_rect().top:
      player.rect.y = player.rect.y - player.vy

    if player.rect.left < screen.get_rect().left:
      player.rect.x = player.rect.x - player.vx

    if player.rect.right > screen.get_rect().right:
      player.rect.x = player.rect.x - player.vx


    #collision between player and and walls
    if player.rect.collidelist(all_walls) >= 0:
      print("Collision !!")
      player.rect.x = player.rect.x - player.vx
      player.rect.y = player.rect.y - player.vy
    
    #bouncing ball code
    if enemy.rect.bottom > screen.get_rect().bottom:
      enemy.speedy = random.randrange(-5, 0)
      enemy.speedx = random.randrange(-5, 5)

    if enemy.rect.top < screen.get_rect().top:
      enemy.speedy = random.randrange(0, 5)
      enemy.speedx = random.randrange(-5, 5)

    if enemy.rect.left < screen.get_rect().left:
      enemy.speedx = random.randrange(0, 5)
      enemy.speedy = random.randrange(-5, 5)

    if enemy.rect.right > screen.get_rect().right:
      enemy.speedx = random.randrange(-5, 0)
      enemy.speedy = random.randrange(-5, 5)

    #bouncing ball code 2
    if enemy2.rect.bottom > screen.get_rect().bottom:
      enemy2.speedy = random.randrange(-5, 0)
      enemy2.speedx = random.randrange(-5, 5)

    if enemy2.rect.top < screen.get_rect().top:
      enemy2.speedy = random.randrange(0, 5)
      enemy2.speedx = random.randrange(-5, 5)

    if enemy2.rect.left < screen.get_rect().left:
      enemy2.speedx = random.randrange(0, 5)
      enemy2.speedy = random.randrange(-5, 5)

    if enemy2.rect.right > screen.get_rect().right:
      enemy2.speedx = random.randrange(-5, 0)
      enemy2.speedy = random.randrange(-5, 5)

    #fill the screen
    screen.fill((0, 0, 0))

    #draw the sprites
    sprites.draw(screen)
    wall_list.draw(screen)
    enemys.draw(screen)

    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

