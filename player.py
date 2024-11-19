from settings import *
from support import animation_parser

class Player:
    def __init__ (self, x, y, max_hp):
        self.animations = {
            'IDLE' : animation_parser('Assets/Player/IDLE.png', 7, 96, 84, 2.5),
            'ATTACK 1' : animation_parser('Assets/Player/ATTACK 1.png', 6, 96, 84, 2.5)
        }
        self.actions = {}

        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.alive = True

        self.image = self.animations['IDLE'][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, dt):
        pass

    def draw_player(self, screen): screen.blit(self.image, self.rect)

    