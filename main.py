from settings import *
from player import Player
from button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")
running = True

background = pygame.image.load('Assets/Background/Cavern.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
screen.fill(COLORS['GREY'])

def draw_bg(): screen.blit(background, (0,0))

      
knight = Player(250, 420, 300)
button = Button('Assets/Buttons/border 2.png', SCREEN_WIDTH//2, 500, 117, 59, 2.5, 'Start')


while running:
    CLOCK.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    button.draw(screen)

    pygame.display.update()
pygame.quit()

    
    



