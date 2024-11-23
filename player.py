from settings import *
from support import animation_parser

class Knight(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        super().__init__()

        self.animations = {
            'IDLE' : [animation_parser('Assets/Player/IDLE.png', 7, 96, 84, 2.5), 0],
            'DEATH' : [animation_parser('Assets/Player/DEATH.png', 12, 96, 84, 2.5), 0],
            'ATTACK 1' : [animation_parser('Assets/Player/ATTACK 1.png', 6, 96, 84, 2.5), 30],
            'ATTACK 2' : [animation_parser('Assets/Player/ATTACK 2.png', 5, 96, 84, 2.5), 40],
            'ATTACK 3' : [animation_parser('Assets/Player/ATTACK 3.png', 6, 96, 84, 2.5), 50],
        }
        
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True

        self.image = self.animations['IDLE'][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.update_time = pygame.time.get_ticks()
        self.curr_frame = 0

    def update(self, action):
        cooldown = 100
        self.image = self.animations[action][0][self.curr_frame]

        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.curr_frame += 1

        if self.curr_frame >= len(self.animations[action][0]):
            self.curr_frame = 0

    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def attack (self, attack_name, target):
        damage = self.animations[attack_name][1]
        target.curr_hp -= damage




    