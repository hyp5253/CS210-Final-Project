from settings import *
from support import *
from entity import Knight, Demon
from healthbar import Healthbar
from button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")

background = pygame.image.load('Assets/Background/Cavern.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
screen.fill(COLORS['GREY'])
      
knight = Knight(250, 420, 300) # going to be a global variable (any updates will be tracked)
demon = Demon(800, 420, 300)

knight_healthbar = Healthbar(SCREEN_WIDTH//6, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)
demon_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, demon.max_hp, demon.max_hp)

""" if knight.alive and turn[0] == knight:
            cooldown += 1
            if cooldown >= wait:
                knight.action = 'ATTACK 2'
                
                turn.append(turn.pop(0))
                cooldown = 0

          
        
        elif demon.alive and turns[0] == demon:
            cooldown += 1
            if cooldown >= wait:
                demon.attack('ATTACK', knight)
                turns.append(turns.pop(0))
                cooldown = 0 """

def test():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, background)

        knight.update()
        knight.draw_entity(screen)
        demon.update()
        demon.draw_entity(screen)

        
        test1 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6), 600, 20, 20))
        test2 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6)+30, 600, 20, 20))
        test3 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6)+60, 600, 20, 20))

        if test1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 1', demon)
        if test2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 2', demon)
        if test3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 3', demon)
            
       

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        demon_healthbar.draw_bar(demon.curr_hp, screen)

        

        pygame.display.update()


def main_menu():
    start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 450, 117, 59, 2.5, 'Start')
    skills = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 600, 117, 59, 2.5, 'Skills')

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









