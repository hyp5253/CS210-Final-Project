from settings import *
from player import Player


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")
running = True

clock = pygame.time.Clock()
fps = 60

background = pygame.image.load('Assets/Background/Cavern.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
screen.fill(COLORS['GREY'])


def draw_bg(): screen.blit(background, (0,0))
      

knight = Player(250, 420, 300)
# turn_queue = [knight]
# action_cooldown = 0
# action_wait_time = 90

while running:
    clock.tick(fps)
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    knight.update('DEATH')
    knight.draw_player(screen)

    # if knight.alive == True:
    #     if turn_queue[0] == knight:
    #         turn_queue.append(turn_queue.pop(0))
    #         if action_cooldown >= action_wait_time:
    #             knight.attack()

    pygame.display.update()
pygame.quit()

    
    



