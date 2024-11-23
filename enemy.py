from settings import *
from support import animation_parser

class Demon(pygame.sprite.Sprite):
    def __init__ (self, x, y, max_hp):
        super().__init__()

        self.animations = {
            'IDLE' : animation_parser('Assets/Enemies/Demon/IDLE.png', 4, 81, 71, 1),
            'ATTACK' : [animation_parser('Assets/Enemies/Demon/ATTACK.png', 8, 81, 71, 1), 25]
        }
        
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True

        self.image = self.animations['IDLE'][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.update_time = pygame.time.get_ticks()
        self.curr_frame = 0

    def update(self, action):
        cooldown = 100
        self.image = self.animations[action][self.curr_frame]

        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.curr_frame += 1

        if self.curr_frame >= len(self.animations[action]):
            self.curr_frame = 0

    def draw_entity(self, screen): screen.blit(self.image, self.rect)

    def attack (self, attack_name, target):
        damage = self.animations[attack_name][1]
        target.curr_hp -= damage
