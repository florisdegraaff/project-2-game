import pkg.foundation.essentials as essentials
import pkg.foundation.display as display

from .spritesheet import *
from .settings import *
pygame = essentials.pygame
class Text(pygame.sprite.Sprite):

    def __init__(self, speech_balloon_object, font, font2, reader, highlighted_answer):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('pkg/level1/images/spritesheet.png')
        self.text_highlighted = 153, 153, 153
        self.text_not_highlighted = 219,219,219

        if speech_balloon_object.amount_of_columns == 1:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))

        if speech_balloon_object.amount_of_columns == 2:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))

        if speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 0:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))

        if speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 1:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))

        if speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 2:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))

        if speech_balloon_object.amount_of_columns == 3 and highlighted_answer == 3:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))

        if speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 0:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 1:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 2:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 3:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))

        if speech_balloon_object.amount_of_columns == 4 and highlighted_answer == 4:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 620))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 0:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 1:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 2:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 3:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 4:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 5 and highlighted_answer == 5:
            display.window.blit(font.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 560))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 590))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 620))
            display.window.blit(font.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 1:
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_highlighted), (335, 530))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_highlighted), (335, 550))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 580))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 600))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 630))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][5], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 2:
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 550))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_highlighted), (335, 580))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_highlighted), (335, 600))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_not_highlighted), (335, 630))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][5], False, BLACK, self.text_not_highlighted), (335, 650))

        if speech_balloon_object.amount_of_columns == 6 and highlighted_answer == 3:
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][0], False, BLACK, self.text_not_highlighted), (335, 530))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][1], False, BLACK, self.text_not_highlighted), (335, 550))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][2], False, BLACK, self.text_not_highlighted), (335, 580))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][3], False, BLACK, self.text_not_highlighted), (335, 600))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][4], False, BLACK, self.text_highlighted), (335, 630))
            display.window.blit(font2.render(reader[speech_balloon_object.current_row][5], False, BLACK, self.text_highlighted), (335, 650))
