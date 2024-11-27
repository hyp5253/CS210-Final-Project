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

