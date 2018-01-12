import pkg.foundation.essentials as essentials

pygame = essentials.pygame

import os

from pygame.math import Vector2

from itertools import cycle

width = 1280
height = 720

class Enemy3(pygame.sprite.Sprite):

    def __init__(self, pos, waypoints, *groups):
        super(Enemy3, self).__init__(*groups)
        #for moving right animation
        images = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/enemyright1","pkg/level2/images/enemyright2", "pkg/level2/images/enemyright1", "pkg/level2/images/enemyright3")]
        self.images = cycle(images)
        self.image = next(self.images)
        #timer for animated sprite
        self.timer = 0
        self.frame_duration = 250 #250 = about 15 frames at 60 fps
        #for moving left animation
        images2 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/enemyleft1","pkg/level2/images/enemyleft2", "pkg/level2/images/enemyleft1", "pkg/level2/images/enemyleft3")]
        self.images2 = cycle(images2)
        self.image = next(self.images2)
        #for moving up animation
        images3 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/enemyup1","pkg/level2/images/enemyup2", "pkg/level2/images/enemyup1", "pkg/level2/images/enemyup3")]
        self.images3 = cycle(images3)
        self.image = next(self.images3)
        #for moving down animation
        images4 = [pygame.image.load("{}.png".format(name)).convert_alpha()
                  for name in ("pkg/level2/images/enemydown1","pkg/level2/images/enemydown2", "pkg/level2/images/enemydown1", "pkg/level2/images/enemydown3")]
        self.images4 = cycle(images4)
        self.image = next(self.images4)
#######################################################

        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0,0)
        self.max_speed = 5
        self.pos = Vector2(pos)
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 10
        self.rect.x = width / 2
        self.rect.y = height / 2

    def update(self):
# A vector pointing from self to the target.
        heading = self.target - self.pos
        distance = heading.length()  # Distance to the target.
        heading.normalize_ip()
        if distance <= 2:  # We're closer than 2 pixels.
          # Increment the waypoint index to swtich the target.
          # The modulo sets the index back to 0 if it's equal to the length.
          self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
          self.target = self.waypoints[self.waypoint_index]
        if distance <= self.target_radius:
                # If we're approaching the target, we slow down.
          self.vel = heading * (distance / self.target_radius * self.max_speed)
        else:  # Otherwise move with max_speed.
          self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos
    #counter for animation
    def counter(self, dt):
        #right
        if self.vel.x > 4.9 and self.vel.y < 1:
            self.timer += dt
            while self.timer >= self.frame_duration:
                self.timer -= self.frame_duration
                self.image = next(self.images)
        #left
        if self.vel.x < -4.9 and self.vel.y < 1:
            self.timer += dt
            while self.timer >= self.frame_duration:
                self.timer -= self.frame_duration
                self.image = next(self.images2)
        #up
        if self.vel.x < 2 and self.vel.y < -4.8:
                self.timer += dt
                while self.timer >= self.frame_duration:
                    self.timer -= self.frame_duration
                    self.image = next(self.images3)
        #down
        if self.vel.x < 2 and self.vel.y > 4.8:
            self.timer += dt
            while self.timer >= self.frame_duration:
                self.timer -= self.frame_duration
                self.image = next(self.images4)
