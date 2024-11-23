from settings import *
from support import *
from player import Knight
from healthbar import Healthbar
from enemy import Demon
from button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")

background = pygame.image.load('Assets/Background/Cavern.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
screen.fill(COLORS['GREY'])
      
knight = Knight(250, 420, 300)
demon = Demon(770, 420, 300)
start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 450, 117, 59, 2.5, 'Start')
skills = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 600, 117, 59, 2.5, 'Skills')

knight_healthbar = Healthbar(SCREEN_WIDTH//6, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)
demon_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, demon.max_hp, demon.max_hp)



def test():
    running = True
    turn_queue = [knight, demon]
    cooldown = 0
    wait = 100    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, background)

        knight.update('IDLE')
        knight.draw_entity(screen)        
        
        demon.update('IDLE')
        demon.draw_entity(screen)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        demon_healthbar.draw_bar(demon.curr_hp, screen) 

        pygame.display.update()


def main_menu():
    while True:
        CLOCK.tick(FPS)

        screen.fill(COLORS['GREY'])
        draw_title(screen, 'Dungeon Destroyer', 'white', SCREEN_WIDTH//2, 275)

        if start_button.draw(screen):
            test()
        if skills.draw(screen):
            print('skill tree')
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            
        pygame.display.update()

main_menu()








