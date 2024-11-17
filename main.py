import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Data Structure Destroyer")


background = pygame.image.load(os.path.join('Assets', 'Background', 'Zone-202-big.png')).convert_alpha()
background = pygame.transform.scale(background, (1000, 500))

def draw_bg(): screen.blit(background, (0,0))


gameLoop = True
while gameLoop:

    draw_bg()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    pygame.display.update()

pygame.quit()

