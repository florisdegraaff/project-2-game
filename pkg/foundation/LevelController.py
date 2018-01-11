import pkg.foundation.display as display
import pkg.foundation.essentials as essentials

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
        global current_level
        current_level = level
        if self.levels[level].tutorial():
            completed = False
            while not completed:
                completed = self.levels[level].run()
            current_level = current_level + 1
            if essentials.running:
                if current_level <= 4:
                    self.load_level(current_level)
                else:
                    menu.run()

    def start_game (self):
        level = menu.run()
        self.load_level(level)
