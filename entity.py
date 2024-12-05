from settings import *
import random
from support import animation_parser

class Knight(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp, max_armor):
        pygame.sprite.Sprite().__init__()

        self.animations = {
            'IDLE' : [animation_parser('Assets/Player/IDLE.png', 7, 96, 84, 2.5), 0],
            'HURT' : [animation_parser('Assets/Player/HURT.png', 4, 96, 84, 2.5), 0],
            'DEATH' : [animation_parser('Assets/Player/DEATH.png', 12, 96, 84, 2.5), 0],
            'ATTACK 1' : [animation_parser('Assets/Player/ATTACK 1.png', 6, 96, 84, 2.5), 30],
            'ATTACK 2' : [animation_parser('Assets/Player/ATTACK 2.png', 5, 96, 84, 2.5), 45],
            'ATTACK 3' : [animation_parser('Assets/Player/ATTACK 3.png', 6, 96, 84, 2.5), 75],
            'DEFEND' : [animation_parser('Assets/Player/DEFEND.png', 6, 96, 84, 2.5), 0]
        }

        self.action = 'IDLE'
        self.defense = False
        self.curr_armor = max_armor
        self.max_armor = max_armor

        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True
        
        self.image = self.animations[self.action][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.update_time = pygame.time.get_ticks()
        self.curr_frame = 0

        self.progress = {
            'wolf' : False,
            'slime' : False,
            'demon' : False
        }

    def update(self):
        cooldown = 100
        self.image = self.animations[self.action][0][self.curr_frame]

        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.curr_frame += 1

        if self.curr_frame >= len(self.animations[self.action][0]):
            if self.action is not 'DEATH':
                self.curr_frame = 0
                self.update_time = pygame.time.get_ticks()
                self.action = 'IDLE'
            else:
                self.curr_frame = len(self.animations['DEATH'][0]) - 1
                
    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def attack (self, action, target):
        self.curr_frame = 0
        self.action = action
        self.update_time = pygame.time.get_ticks()

        damage = self.animations[action][1]
        target.curr_hp -= damage
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

    def defend(self): 
        self.curr_frame = 0
        self.defense= True
        self.action = 'DEFEND'
        self.update_time = pygame.time.get_ticks()

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp, animations):
        pygame.sprite.Sprite().__init__()

        self.animations = animations
        
        self.action = 'IDLE'

        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True
        
        self.image = self.animations[self.action][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.update_time = pygame.time.get_ticks()
        self.curr_frame = 0

    def update(self):
        cooldown = 100
        self.image = self.animations[self.action][0][self.curr_frame]

        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.curr_frame += 1

        if self.curr_frame >= len(self.animations[self.action][0]):
            if self.action is not 'DEATH':
                self.curr_frame = 0
                self.update_time = pygame.time.get_ticks()
                self.action = 'IDLE'
            else:
                self.curr_frame = len(self.animations['DEATH'][0]) - 1
                
    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def attack (self, action, target):
        self.curr_frame = 0
        self.action = action
        self.update_time = pygame.time.get_ticks()

        damage = self.animations[action][1]
        if not target.defense:
            target.curr_hp -= damage
        else:
            random_num = random.randint(1, 10)
            if random_num <= 3:
                target.curr_hp -= damage
            target.defense = False
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

class Boss(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp, animations):
        pygame.sprite.Sprite().__init__()

        self.animations = animations
        
        self.action = 'IDLE'

        self.attacks_list = ['SPELL 1', 'ATTACK']

        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True
        
        self.image = self.animations[self.action][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.update_time = pygame.time.get_ticks()
        self.curr_frame = 0

        self.spell = 'SPELL 1'
        self.cast_spell = False

        self.spell_img = self.animations[self.spell][0][0]
        self.spell_rect = self.spell_img.get_rect()
        self.spell_rect.center = (255, 440)
        self.spell_frame = 0

    def update(self):
        cooldown = 100
        self.image = self.animations[self.action][0][self.curr_frame]
        self.spell_img = self.animations[self.spell][0][self.spell_frame]

        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.curr_frame += 1

            if self.cast_spell is True:
                self.spell_frame += 1
            

        if self.curr_frame >= len(self.animations[self.action][0]):
            if self.action is not 'DEATH':
                self.curr_frame = 0
                self.update_time = pygame.time.get_ticks()
                self.action = 'IDLE'

                self.spell_frame = 0
                self.cast_spell = False
            else:
                self.curr_frame = len(self.animations['DEATH'][0]) - 1
                
    def draw_entity(self, screen): 
        screen.blit(self.image, self.rect)
        screen.blit(self.spell_img, self.spell_rect)

    def attack (self, action, target):
        if action == 'SPELL 1':
            self.action = 'IDLE'
            self.spell = 'SPELL 1'
            self.cast_spell = True
        else:
            self.action = action

        self.curr_frame = 0
        self.spell_frame = 0
        self.update_time = pygame.time.get_ticks()

        damage = self.animations[action][1]
        if not target.defense:
            if target.curr_armor > 0 and action != 'SPELL 1':
                target.curr_armor -= damage
            else:
                target.curr_hp -= damage
        else:
            random_num = random.randint(1, 10)
            if random_num <= 3:
                target.curr_hp -= damage
            target.defense = False

        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

