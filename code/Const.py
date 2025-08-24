import pygame.constants

#C
COLOR_RED = (250,0,0)
COLOR_WHITE = (255,255,255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1': 4,
    'Enemy1': 2,
    'Enemy2': 1,

}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# S
SPAWN_TIME = 4000
#W

WIN_WIDTH = 800
WIN_HEIGHT = 533