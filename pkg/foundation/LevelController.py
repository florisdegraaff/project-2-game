import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

display.prepare_screen()

import pkg.menu.main as menu
import pkg.level1.main as level1
import pkg.level2.main as level2
import pkg.level3.main as level3
import pkg.level4.main as level4
import pkg.level5.main as level5

class LevelController:

    current_level = 0

    levels = [
        level1,
        level2,
        level3,
        level4,
        level5
    ]

    def load_level (self, level = 0):
        self.current_level = level
        completed = False
        while not completed:
            completed = self.levels[level].run()
        self.current_level = self.current_level + 1
        self.load_level(self.current_level)            

    def start_game (self):
        level = menu.run()
        self.load_level(level)
