from settings import *
import random
from support import animation_parser

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
