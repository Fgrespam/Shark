import pygame.constants

# C
COLOR_RED = (250, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 0,
    'Level2Bg0': 1,
    'Level2Bg1': 0,
    'Player1': 4,
    'Enemy1': 1,
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# S
SPAWN_TIME = 5000

# T
TIMEOUT_STEP = 100  # 100 ms
TIMEOUT_LEVEL = 60000  # Tempo da fase

# W

WIN_WIDTH = 800
WIN_HEIGHT = 533

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 100),
             'Label': (WIN_WIDTH / 2, 120),
             'Name': (WIN_WIDTH / 2, 150),
             0: (WIN_WIDTH / 2, 180),
             1: (WIN_WIDTH / 2, 210),
             2: (WIN_WIDTH / 2, 240),
             3: (WIN_WIDTH / 2, 270),
             4: (WIN_WIDTH / 2, 300),
             5: (WIN_WIDTH / 2, 330),
             6: (WIN_WIDTH / 2, 360),
             7: (WIN_WIDTH / 2, 390),
             8: (WIN_WIDTH / 2, 420),
             9: (WIN_WIDTH / 2, 450),
             }
