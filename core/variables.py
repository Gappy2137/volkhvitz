"""Constants and variables."""
from pathlib import Path
from main import *

"""Constants."""
DIR = str(Path(__file__).parents[1])

# Menu constants.
OPTIONS = ['start', 'info', 'exit']
RESOLUTION = [640, 480]

MENU_IMG = pygame.image.load(os.path.join(DIR + r'\spritesheet', 'menu.png'))
ARROW_IMG = pygame.image.load(os.path.join(DIR + r'\spritesheet', 'arrow.png'))

PLAYER_SPRITES = [pygame.image.load(os.path.join(DIR + r'\spritesheet', 'player_frame_0.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet', 'player_frame_1.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet', 'player_frame_left.png')),
                  pygame.image.load(os.path.join(DIR + r'\spritesheet', 'player_frame_right.png'))]

# Game constants.
FPS = 60

"""Variables."""
# Menu variables.
opt_num = 0
opt_check = OPTIONS[opt_num]

in_menu = True
in_game = False
in_info = False
