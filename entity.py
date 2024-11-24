from settings import *
from support import animation_parser


class Knight(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        pygame.sprite.Sprite().__init__()

        self.animations = {
            'IDLE' : [animation_parser('Assets/Player/IDLE.png', 7, 96, 84, 2.5), 0],
            'DEATH' : [animation_parser('Assets/Player/DEATH.png', 12, 96, 84, 2.5), 0],
            'ATTACK 1' : [animation_parser('Assets/Player/ATTACK 1.png', 6, 96, 84, 2.5), 30],
            'ATTACK 2' : [animation_parser('Assets/Player/ATTACK 2.png', 5, 96, 84, 2.5), 40],
            'ATTACK 3' : [animation_parser('Assets/Player/ATTACK 3.png', 6, 96, 84, 2.5), 50],
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
            self.curr_frame = 0
            self.update_time = pygame.time.get_ticks()
            self.action = 'IDLE'

    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def attack (self, action, target):
        self.curr_frame = 0
        self.action = action
        damage = self.animations[action][1]
        target.curr_hp -= damage
        self.update_time = pygame.time.get_ticks()


class Demon(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        pygame.sprite.Sprite().__init__()

        self.animations = {
            'IDLE' : [animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 1), 0]
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
            self.curr_frame = 0

    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def action (self, action_name, target):
        damage = self.animations[action_name][1]
        target.curr_hp -= damage





    