import pygame.constants

#C
COLOR_RED = (250,0,0)
COLOR_WHITE = (255,255,255)

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
    'Enemy1': 8,
    }

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# S
SPAWN_TIME = 5000


# T
TIMEOUT_STEP = 100 #100 ms
TIMEOUT_LEVEL =5000 #Tempo da fase

#W

WIN_WIDTH = 800
WIN_HEIGHT = 533

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 100),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 150),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }