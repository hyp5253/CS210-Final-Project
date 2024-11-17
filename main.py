import pygame
import os
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Data Structure Destroyer")


background = pygame.image.load(os.path.join('Assets','Background','Cavern.png')).convert_alpha()
background = pygame.transform.scale(background, (1080, 500))
def draw_bg(): screen.blit(background, (0,0))


running = True
while running:

    draw_bg()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

