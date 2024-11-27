from settings import *
from support import *
from entity import Knight, Demon, Slime
from healthbar import Healthbar
from skills import *
from menu_button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Placeholder")

cavern = pygame.image.load('Assets/Background/Cavern.png').convert_alpha()
cavern = pygame.transform.scale(cavern, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
forest = pygame.image.load('Assets/Background/Dead_Forest.png').convert_alpha()
forest = pygame.transform.scale(forest, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
panel = pygame.image.load('Assets/Background/panel.png').convert_alpha()
panel = pygame.transform.scale(panel, (SCREEN_WIDTH, BOTTOM_PANEL))
screen.fill(COLORS['GREY'])
      
knight = Knight(250, 420, 300) # going to be a global variable (any updates will be tracked)
knight_healthbar = Healthbar(SCREEN_WIDTH//6, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)

def level_1():
    knight.curr_hp = knight.max_hp
    slime = Slime(780, 430, 300)
    slime_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, slime.max_hp, slime.max_hp)

    running = True
    turn = [knight, slime]
    wait = 100
    cooldown = 0

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        slime_healthbar.draw_bar(slime.curr_hp, screen)

        for skill in skill_tree:
            skill.draw_skill(screen)

        knight.update()
        knight.draw_entity(screen)
        slime.update()
        slime.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if attack_1.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 1', slime)
                turn.append(turn.pop(0))
            
            if attack_2.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 2', slime)
                turn.append(turn.pop(0))

            if attack_3.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.attack('ATTACK 3', slime)
                turn.append(turn.pop(0))

            if defend.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

        elif slime.alive and turn[0] == slime:
            cooldown += 1
            if cooldown >= wait:
                slime.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        pygame.display.update()

def level_2():
    knight.curr_hp = knight.max_hp
    demon = Demon(800, 400, 300)
    demon_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, demon.max_hp, demon.max_hp)

    running = True
    turn = [knight, demon]
    wait = 150
    cooldown = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        demon_healthbar.draw_bar(demon.curr_hp, screen)

        knight.update()
        knight.draw_entity(screen)
        demon.update()
        demon.draw_entity(screen)
        
        test1 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6), 600, 20, 20))
        test2 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6)+30, 600, 20, 20))
        test3 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6)+60, 600, 20, 20))
        test4 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//6)+90, 600, 20, 20))


        if knight.alive and turn[0] is knight:
            if test1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                    knight.attack('ATTACK 1', demon)
                    turn.append(turn.pop(0))

            if test2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                    knight.attack('ATTACK 2', demon)
                    turn.append(turn.pop(0))

            if test3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                    knight.attack('ATTACK 3', demon)
                    turn.append(turn.pop(0))

            if test4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                    knight.defend()
                    turn.append(turn.pop(0))

        elif demon.alive and turn[0] == demon:
                cooldown += 1
                if cooldown >= wait:
                    demon.attack('ATTACK', knight)
                    turn.append(turn.pop(0))
                    cooldown = 0


        pygame.display.update()

def map():
    running = True

    while running:
        screen.fill(COLORS['GREY'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        lvl1 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//2), 100, 20, 20))
        if lvl1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_1()

        lvl2 = pygame.draw.rect(screen, 'red', ((SCREEN_WIDTH//2), 200, 20, 20))
        if lvl2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_2()
        

        pygame.display.update()

def main_menu():
    start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 450, 117, 59, 2.5, 'Start')
    skills = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 600, 117, 59, 2.5, 'Skills')

    while True:
        CLOCK.tick(FPS)

        screen.fill(COLORS['GREY'])
        draw_title(screen, 'Dungeon Destroyer', 'white', SCREEN_WIDTH//2, 275)

        if start_button.draw(screen):
            map()
        if skills.draw(screen):
            print('skill tree')
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            
        pygame.display.update()

main_menu()









