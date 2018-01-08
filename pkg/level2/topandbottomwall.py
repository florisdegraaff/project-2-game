class TopAndBottomWall(pg.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pg.image.load("topandbottomwall.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
