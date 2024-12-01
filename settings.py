import pygame

BOTTOM_PANEL = 220
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 500 + BOTTOM_PANEL

CLOCK = pygame.time.Clock()
FPS = 60

BUTTON_FONT = pygame.font.init()
BUTTON_FONT = pygame.font.Font('Assets/Font/Jacquard12-Regular.ttf', 80)

TITLE_FONT = pygame.font.init()
TITLE_FONT = pygame.font.Font('Assets/Font/Jacquard12-Regular.ttf', 140)

COLORS = {
    'BLACK' : (0,0,0),
    'GREY' : (50,50,50)
}

cavern = pygame.image.load('Assets/Background/Cavern.png')
cavern = pygame.transform.scale(cavern, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
forest = pygame.image.load('Assets/Background/Dead_Forest.png')
forest = pygame.transform.scale(forest, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
panel = pygame.image.load('Assets/Background/panel.png')
panel = pygame.transform.scale(panel, (SCREEN_WIDTH, BOTTOM_PANEL))
