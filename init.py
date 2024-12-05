from pygame import mixer
from settings import *
from support import *
from skills import *
from upgrades import *
from map_graph import *
from entity import Knight, Enemy, Boss
from bar import Healthbar, Armor
from menu_button import Button
from random import choice, randint

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

main_theme = mixer.Sound('Assets/Audio/main_theme.mp3')
main_theme.set_volume(0.2)
main_theme.play(-1)

boss_theme = mixer.Sound('Assets/Audio/boss_theme.mp3')
boss_theme.set_volume(0.1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Destroyer")
screen.fill(COLORS['GREY'])
      
knight = Knight(250, 420, 400, 50) 
knight_healthbar = Healthbar((SCREEN_WIDTH//6)+20, SCREEN_HEIGHT-BOTTOM_PANEL+25, knight.max_hp, knight.max_hp)
knight_armor = Armor((SCREEN_WIDTH//6)+20, SCREEN_HEIGHT-BOTTOM_PANEL+160, knight.max_armor, knight.max_armor)

slime_animations = {
            'IDLE' : [animation_parser_r('Assets/Enemies/Slime/IDLE.png', 4, 64, 64, 4), 0],
            'ATTACK' : [animation_parser_r('Assets/Enemies/Slime/ATTACK.png', 4, 64, 64, 4), 50],
            'HURT' : [animation_parser_r('Assets/Enemies/Slime/HURT.png', 4, 64, 64, 4), 0],
            'DEATH' : [animation_parser_r('Assets/Enemies/Slime/DEATH.png', 4, 64, 64, 4), 0],
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

cavern = pygame.image.load('Assets/Background/Cavern.png')
cavern = pygame.transform.scale(cavern, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
forest = pygame.image.load('Assets/Background/Dead_Forest.png')
forest = pygame.transform.scale(forest, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
panel = pygame.image.load('Assets/Background/panel.png')
panel = pygame.transform.scale(panel, (SCREEN_WIDTH, BOTTOM_PANEL))