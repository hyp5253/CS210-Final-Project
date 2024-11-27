from settings import *
import random
from support import animation_parser, animation_parser_r

class Knight(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
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
        target.curr_hp -= damage
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

    def defend(self): 
        self.curr_frame = 0
        self.action = 'DEFEND'
        self.update_time = pygame.time.get_ticks()

class Demon(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        pygame.sprite.Sprite().__init__()

        self.animations = {
            'IDLE' : [animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 2.5), 0],
            'HURT' : [animation_parser('Assets/Enemies/Demon/HURT.png', 4, 81, 71, 2.5), 0],
            'DEATH' : [animation_parser('Assets/Enemies/Demon/DEATH.png', 6, 81, 71, 2.5), 0],
            'ATTACK' : [animation_parser('Assets/Enemies/Demon/ATTACK.png', 8, 81, 71, 2.5), 30],
        }  
        
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
            if random_num >= 3:
                target.curr_hp -= damage//4
            else:
                target.curr_hp -= damage
            target.defense = False
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

class Slime(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        pygame.sprite.Sprite().__init__()

        self.animations = {
            'IDLE' : [animation_parser_r('Assets/Enemies/Slime/IDLE.png', 4, 64, 64, 3), 0],
            'ATTACK' : [animation_parser_r('Assets/Enemies/Slime/ATTACK.png', 4, 64, 64, 3), 35],
            'HURT' : [animation_parser_r('Assets/Enemies/Slime/HURT.png', 4, 64, 64, 3), 0],
            'DEATH' : [animation_parser_r('Assets/Enemies/Slime/DEATH.png', 4, 64, 64, 3), 0],
        }  
        
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
            if random_num >= 3:
                target.curr_hp -= damage//4
            else:
                target.curr_hp -= damage
            target.defense = False
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'

class Wolf(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        pygame.sprite.Sprite().__init__()

        self.animations = {
           'IDLE' : [animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4), 0],
           'ATTACK' : [animation_parser('Assets/Enemies/Dark Wolf/ATTACK 1.png', 4, 48, 32, 4), 40],
           'HURT' : [animation_parser('Assets/Enemies/Dark Wolf/IDLE.png', 4, 48, 32, 4), 0],
           'DEATH' : [animation_parser('Assets/Enemies/Dark Wolf/DEATH.png', 4, 48, 32, 4), 0],
        
        }  

        self.animations['ATTACK'][0] += (animation_parser('Assets/Enemies/Dark Wolf/ATTACK 1-2.png', 3, 48, 32, 4))
        self.animations['DEATH'][0] += (animation_parser('Assets/Enemies/Dark Wolf/DEATH.png', 4, 48, 32, 4))
        

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
            if random_num >= 3:
                target.curr_hp -= damage//4
            else:
                target.curr_hp -= damage
            target.defense = False
        target.curr_frame = 0
        target.action = 'HURT'
        if target.curr_hp <= 0:
            target.alive = False
            target.action = 'DEATH'