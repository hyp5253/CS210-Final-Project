from settings import *
from support import *
from skills import *
from entity import Knight, Demon, Slime, Wolf
from healthbar import Healthbar
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
      
knight = Knight(250, 420, 400) 
knight_healthbar = Healthbar(SCREEN_WIDTH//6, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)

def level_slime():
    knight.curr_hp = knight.max_hp
    slime = Slime(780, 430, 400)
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

        breadth_first_traversal(attack_1, screen)

        knight.update()
        knight.draw_entity(screen)
        slime.update()
        slime.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if attack_1.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_1.unlocked:
                knight.attack('ATTACK 1', slime)
                turn.append(turn.pop(0))
            
            if attack_2.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_2.unlocked:
                knight.attack('ATTACK 2', slime)
                turn.append(turn.pop(0))

            if attack_3.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_3.unlocked:
                knight.attack('ATTACK 3', slime)
                turn.append(turn.pop(0))

            if defend.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and defend.unlocked:
                knight.defend()
                turn.append(turn.pop(0))

        elif slime.alive and turn[0] == slime:
            cooldown += 1
            if cooldown >= wait:
                slime.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        pygame.display.update()

def level_wolf():
    knight.curr_hp = knight.max_hp
    wolf = Wolf(780, 400, 300)
    wolf_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, wolf.max_hp, wolf.max_hp)

    running = True
    turn = [knight, wolf]
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
        draw_bg(screen, forest)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        wolf_healthbar.draw_bar(wolf.curr_hp, screen)

        breadth_first_traversal(attack_1, screen)

        knight.update()
        knight.draw_entity(screen)
        wolf.update()
        wolf.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if attack_1.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_1.unlocked:
                knight.attack('ATTACK 1', wolf)
                turn.append(turn.pop(0))
            
            if attack_2.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_2.unlocked:
                knight.attack('ATTACK 2', wolf)
                turn.append(turn.pop(0))

            if attack_3.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_3.unlocked:
                knight.attack('ATTACK 3', wolf)
                turn.append(turn.pop(0))

            if defend.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and defend.unlocked:
                knight.defend()
                turn.append(turn.pop(0))

        elif wolf.alive and turn[0] == wolf:
            cooldown += 1
            if cooldown >= wait:
                wolf.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        pygame.display.update()

def level_demon():
    knight.curr_hp = knight.max_hp
    demon = Demon(800, 400, 300)
    demon_healthbar = Healthbar((SCREEN_WIDTH//6)*4, SCREEN_HEIGHT-BOTTOM_PANEL+25, demon.max_hp, demon.max_hp)

    running = True
    turn = [knight, demon]
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
        demon_healthbar.draw_bar(demon.curr_hp, screen)

        breadth_first_traversal(attack_1, screen)

        knight.update()
        knight.draw_entity(screen)
        demon.update()
        demon.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if attack_1.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_1.unlocked:
                knight.attack('ATTACK 1', demon)
                turn.append(turn.pop(0))
            
            if attack_2.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_2.unlocked:
                knight.attack('ATTACK 2', demon)
                turn.append(turn.pop(0))

            if attack_3.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and attack_3.unlocked:
                knight.attack('ATTACK 3', demon)
                turn.append(turn.pop(0))

            if defend.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] and defend.unlocked:
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

    slime_img_list = animation_parser('Assets/Enemies/Slime/IDLE.png', 4, 64, 64, 6)
    slime_img = slime_img_list[0]
    slime_rect = slime_img.get_rect()
    slime_rect.center = (SCREEN_WIDTH//3, 300)

    wolf_img_list = animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4)
    wolf_img = wolf_img_list[0]
    wolf_rect = wolf_img.get_rect()
    wolf_rect.center = (SCREEN_WIDTH//2, 150)

    demon_img_list = animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 2.5)
    demon_img = demon_img_list[0]
    demon_rect = demon_img.get_rect()
    demon_rect.center = ((SCREEN_WIDTH//3)*2, 350)


    while running:
        CLOCK.tick(FPS)
        screen.fill(COLORS['GREY'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        screen.blit(slime_img, slime_rect)
        screen.blit(wolf_img, wolf_rect)
        screen.blit(demon_img, demon_rect)
       
        if wolf_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_wolf()

        if slime_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_slime()

        if demon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            level_demon()
        

        pygame.display.update()

def main_menu():
    start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 450, 117, 59, 2.5, 'Start')
    skills = Button('Assets/UI/border 2.png', SCREEN_WIDTH//2, 600, 117, 59, 2.5, 'Skills')

    while True:
        CLOCK.tick(FPS)

        screen.fill(COLORS['GREY'])
        draw_menu_bg(screen, cavern)
        draw_title(screen, 'Dungeon Destroyer', 'white', SCREEN_WIDTH//2, 275)

        if start_button.draw(screen):
            map()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            
        pygame.display.update()

main_menu()









