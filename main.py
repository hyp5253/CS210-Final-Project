from settings import *
from support import *
from knight import Player, healthbar
from demon import Enemy
from button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")

background = pygame.image.load('Assets/Background/Cavern.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
screen.fill(COLORS['GREY'])
      
knight = Player(250, 420, 300)
demon = Enemy(750, 420, 300)
start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 450, 117, 59, 2.5, 'Start')
skills = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 600, 117, 59, 2.5, 'Skills')

knight_healthbar = healthbar(SCREEN_WIDTH//5, 600, knight.max_hp, knight.max_hp)


    
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

        knight.update('ATTACK 1')
        knight.draw_entity(screen)

        demon.update('ATTACK')
        demon.draw_entity(screen)

        knight_healthbar.draw_bar(knight.curr_hp, screen)

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








