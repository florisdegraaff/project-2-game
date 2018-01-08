import pkg.display as display
import pkg.essentials as essentials

display.prepare_screen()

import pkg.menu.main as menu
import pkg.level1.main as level1
import pkg.level2.main as level2
import pkg.level3.main as level3
import pkg.level4.main as level4
import pkg.level5.main as level5

current_level = 1

if (essentials.running):
    menu.run()
if (essentials.running):
    level1.run()
if (essentials.running):
    level2.run()
if (essentials.running):
    level3.run()
if (essentials.running):
    completed = False
    while not completed:
        completed = level4.run()
if (essentials.running):
    level5.run()
