from pygame import mixer
from settings import *
from support import *
from skills import *
from upgrades import *
from entity import Knight, Enemy, Boss
from bar import Healthbar, Armor
from menu_button import Button
from random import choice

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

main_theme = mixer.Sound('Assets/Audio/main_theme.mp3')
main_theme.set_volume(0.2)
# main_theme.play(-1)

boss_theme = mixer.Sound('Assets/Audio/boss_theme.mp3')
boss_theme.set_volume(0.1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Destroyer")
screen.fill(COLORS['GREY'])
      
knight = Knight(250, 420, 400, 50) 
knight_healthbar = Healthbar((SCREEN_WIDTH//6)+20, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)
knight_armor = Armor((SCREEN_WIDTH//6)+20, SCREEN_HEIGHT-BOTTOM_PANEL+160, knight.max_armor, knight.max_armor)

graph = {'wolf' : ['slime'],
         'slime' : ['wolf', 'demon'],
         'demon' : ['slime']}

slime_animations = {
            'IDLE' : [animation_parser_r('Assets/Enemies/Slime/IDLE.png', 4, 64, 64, 3), 0],
            'ATTACK' : [animation_parser_r('Assets/Enemies/Slime/ATTACK.png', 4, 64, 64, 3), 35],
            'HURT' : [animation_parser_r('Assets/Enemies/Slime/HURT.png', 4, 64, 64, 3), 0],
            'DEATH' : [animation_parser_r('Assets/Enemies/Slime/DEATH.png', 4, 64, 64, 3), 0],
        }  
demon_animations = {
            'IDLE' : [animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 2.5), 0],
            'HURT' : [animation_parser('Assets/Enemies/Demon/HURT.png', 4, 81, 71, 2.5), 0],
            'DEATH' : [animation_parser('Assets/Enemies/Demon/DEATH.png', 6, 81, 71, 2.5), 0],
            'ATTACK' : [animation_parser('Assets/Enemies/Demon/ATTACK.png', 8, 81, 71, 2.5), 60],
            'SPELL 1' : [animation_parser('Assets/Enemies/Demon/SPELL 1-1.png', 6, 32, 32, 3), 45],
        }  
demon_animations['SPELL 1'][0] += animation_parser('Assets/Enemies/Demon/SPELL 1-2.png', 4, 32, 32, 3)
wolf_animations = {
           'IDLE' : [animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4), 0],
           'ATTACK' : [animation_parser('Assets/Enemies/Dark Wolf/ATTACK 1.png', 4, 48, 32, 4), 40],
           'HURT' : [animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4), 0],
           'DEATH' : [animation_parser('Assets/Enemies/Dark Wolf/DEATH.png', 4, 48, 32, 4), 0],
        } 
wolf_animations['ATTACK'][0] += animation_parser('Assets/Enemies/Dark Wolf/ATTACK 1-2.png', 3, 48, 32, 4)
wolf_animations['DEATH'][0] += animation_parser('Assets/Enemies/Dark Wolf/DEATH 1-2.png', 4, 48, 32, 4)

def level_wolf():
    knight.curr_hp = knight.max_hp
    knight.curr_armor = knight.max_armor

    wolf = Enemy(780, 400, 300, wolf_animations)
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
        knight_armor.draw_bar(knight.curr_armor, screen)
        wolf_healthbar.draw_bar(wolf.curr_hp, screen)

        breadth_first_traversal(knife, screen)

        knight.update()
        knight.draw_entity(screen)
        wolf.update()
        wolf.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', wolf)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', wolf)
                else:                                   knight.attack('ATTACK 3', wolf)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

        elif wolf.alive and turn[0] == wolf:
            cooldown += 1
            if cooldown >= wait:
                wolf.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0

        pygame.display.update()

def level_slime():
    knight.curr_hp = knight.max_hp
    knight.curr_armor = knight.max_armor

    slime = Enemy(780, 430, 400, slime_animations)
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
        knight_armor.draw_bar(knight.curr_armor, screen)
        slime_healthbar.draw_bar(slime.curr_hp, screen)

        breadth_first_traversal(knife, screen)

        knight.update()
        knight.draw_entity(screen)
        slime.update()
        slime.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', slime)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', slime)
                else:                                   knight.attack('ATTACK 3', slime)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

        elif slime.alive and turn[0] == slime:
            cooldown += 1
            if cooldown >= wait:
                slime.attack('ATTACK', knight)
                turn.append(turn.pop(0))
                cooldown = 0


        pygame.display.update()

def level_demon():
    # main_theme.fadeout(500)
    # boss_theme.play(-1)

    knight.curr_hp = knight.max_hp
    knight.curr_armor = knight.max_armor

    demon = Boss(800, 400, 700, demon_animations)
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
                # boss_theme.fadeout(500)
                # main_theme.play(-1)
                running = False

        screen.fill(COLORS['GREY'])
        draw_bg(screen, cavern)
        draw_panel(screen, panel)

        knight_healthbar.draw_bar(knight.curr_hp, screen)
        knight_armor.draw_bar(knight.curr_armor, screen)
        demon_healthbar.draw_bar(demon.curr_hp, screen)

        breadth_first_traversal(knife, screen)

        knight.update()
        knight.draw_entity(screen)
        demon.update()
        demon.draw_entity(screen)


        if knight.alive and turn[0] is knight: 
            if curr_weapon[0][2].rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                
                if curr_weapon[0][2] is knife:          knight.attack('ATTACK 1', demon)
                elif curr_weapon[0][2] is wooden_sword: knight.attack('ATTACK 2', demon)
                else:                                   knight.attack('ATTACK 3', demon)

                turn.append(turn.pop(0))
            

            if wooden_shield.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                knight.defend()
                turn.append(turn.pop(0))

        elif demon.alive and turn[0] == demon:
            cooldown += 1
            if cooldown >= wait:
                action = choice(demon.attacks_list)
                demon.attack(action, knight)
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

def skills_menu():
    running = True

    while running:
        CLOCK.tick(FPS)
        screen.fill(COLORS['GREY'])

        draw_upgrades_menu(screen)

        if weapon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if weapon_upgrades:
                curr_weapon[0][2].equipped = False
                curr_weapon[0] = weapon_upgrades.pop(0)
                curr_weapon[0][2].equipped = True

        if shield_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if shield_upgrades:
                curr_shield[0][2].equipped = False
                curr_shield[0] = shield_upgrades.pop(0)
                curr_shield[0][2].equipped = True
                knight.max_armor += 100  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        pygame.display.update()
        
def main_menu():
    start_button = Button('Assets/UI/border 2.png', SCREEN_WIDTH//3+30, 450, 117, 59, 2.5, 'Start')
    skills = Button('Assets/UI/border 2.png', (SCREEN_WIDTH//3)*2-30, 450, 117, 59, 2.5, 'Skills')

    while True:
        CLOCK.tick(FPS)

        screen.fill(COLORS['GREY'])
        draw_menu_bg(screen, cavern)
        draw_title(screen, 'Dungeon Destroyer', 'white', SCREEN_WIDTH//2, 275)

        if start_button.draw(screen):
            map()
        if skills.draw(screen):
            skills_menu()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            
        pygame.display.update()

if __name__ == "__main__":
    main_menu()









