class Enemy(pg.sprite.Sprite):

    def __init__(self, pos, waypoints, *groups):
        super().__init__(*groups)
        self.image = pg.image.load("enemy.png")
        self.image = pg.transform.scale(self.image, (int(50), int(50)))
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0,0)
        self.max_speed = 5
        self.pos = Vector2(pos)
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 50
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

