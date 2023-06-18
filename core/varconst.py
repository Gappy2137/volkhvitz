"""Constants and variables."""
from imports import *
from pathlib import Path

"""Constants."""
# Game directory.
DIR = str(Path(__file__).parents[1])

# Menu constants.
OPTIONS = ['start', 'info', 'exit']
RESOLUTION = [640, 480]

MENU_IMG = pygame.image.load(os.path.join(DIR + r'\spritesheet', 'menu.png'))
ARROW_IMG = pygame.image.load(os.path.join(DIR + r'\spritesheet', 'arrow.png'))
INFO_IMG = pygame.image.load(os.path.join(DIR + r'\spritesheet', 'info.png'))

# Game constants.
FPS = 120

# HUD constants.
TEXT_WIDTH = 16
TEXT_HEIGHT = 32
POWER_X = 416
POWER_Y = 160
SCORE_X = 512
SCORE_Y = 64
LIVES_X = 416
LIVES_Y = 240
BARS_LEFT = 10
BARS_TOP = 10
BARS_RIGHT = 388
BARS_BOTTOM = 472

"""Variables."""
# Menu variables.
opt_num = 0
opt_check = OPTIONS[opt_num]

in_menu = True
in_game = False
in_info = False

