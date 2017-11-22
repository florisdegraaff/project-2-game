import pkg.level1.main as level1
import pkg.level2.main as level2
import pkg.level3.main as level3
import pkg.level4.main as level4
import pkg.level5.main as level5
import pkg.display as display
import pkg.essentials as essentials

current_level = 1

display.prepare_screen()

if (essentials.running):
    level1.run()
if (essentials.running):
    level2.run()
if (essentials.running):
    level3.run()
if (essentials.running):
    level4.run()
if (essentials.running):
    level5.run()
