from settings import *
from support import animation_parser

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super.__init__()
        self.image
        self.rect

    def update(self, dt):
        self.image = self.animation[0]


    def get_animation_list(self, path):
        self.animation = animation_parser(path)