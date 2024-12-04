from settings import *
from skills import * 

character_img_static = pygame.image.load('Assets/Player/IDLE_Upgrade_menu.png')

character_img_static = pygame.transform.scale(character_img_static, (96*5, 84*5))
character_rect = character_img_static.get_rect()
character_rect.center = ((SCREEN_WIDTH//5), (SCREEN_HEIGHT)//2)


icon1 = pygame.image.load('Assets/UI/Action Border.png')
icon1 = pygame.transform.scale(icon1, (64*3, 64*3))
icon1_rect = icon1.get_rect()
icon1_rect.center = ((SCREEN_WIDTH//5)*3, SCREEN_HEIGHT//2)

weapon = pygame.image.load('Assets/Misc/Knife.png')
weapon = pygame.transform.scale(weapon, (32*3, 32*3))
weapon_rect = weapon.get_rect()
weapon_rect.center = ((SCREEN_WIDTH//5)*3, SCREEN_HEIGHT//2)

weapon_up1 = pygame.image.load('Assets/Misc/Wooden Sword.png')
weapon_up1 = pygame.transform.scale(weapon_up1, (32*3, 32*3))

weapon_up2 = pygame.image.load('Assets/Misc/Iron Sword.png')
weapon_up2 = pygame.transform.scale(weapon_up2, (32*3, 32*3))

curr_weapon = [(weapon, weapon_rect, knife)]
weapon_upgrades = [(weapon_up1, weapon_rect, wooden_sword), (weapon_up2, weapon_rect, iron_sword)]


icon2 = pygame.image.load('Assets/UI/Action Border.png')
icon2 = pygame.transform.scale(icon2, (64*3, 64*3))
icon2_rect = icon2.get_rect()
icon2_rect.center = ((SCREEN_WIDTH//5)*4, SCREEN_HEIGHT//2)

shield = pygame.image.load('Assets/Misc/Wooden Shield.png')
shield = pygame.transform.scale(shield, (32*3, 32*3))
shield_rect = shield.get_rect()
shield_rect.center = ((SCREEN_WIDTH//5)*4, SCREEN_HEIGHT//2)

shield_up1 = pygame.image.load('Assets/Misc/Iron Shield.png')
shield_up1 = pygame.transform.scale(shield_up1, (32*3, 32*3))

curr_shield = [(shield, shield_rect, wooden_shield)]
shield_upgrades = [(shield_up1, shield_rect, iron_shield)]


def draw_upgrades_menu(screen):
    screen.blit(character_img_static, character_rect)
    screen.blit(icon1, icon1_rect)
    screen.blit(icon2, icon2_rect)
    screen.blit(curr_weapon[0][0], curr_weapon[0][1])
    screen.blit(curr_shield[0][0], curr_shield[0][1])
