class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("character.png")
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
