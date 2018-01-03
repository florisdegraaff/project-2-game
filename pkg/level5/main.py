from .. import essentials
from .. import display

running = True
pygame = essentials.pygame

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

clock = pygame.time.Clock()

W, H = 1280, 800
HW, HH = W / 2, H / 2
AREA = W * H
        
class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))

        self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),])
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

choepah = spritesheet("choppah.png", 6, 1)

def run():
    global running
    global pygame

    while running == True:

        # Input
        for event in pygame.event.get():

            # Load in the fundemental functions in the game
            running = essentials.run_essentials(event)

        # Output


        # Update the display to show the changes you made
        display.update()
