from settings import *

class Healthbar():
    def __init__ (self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw_bar(self, hp, screen):
        self.hp = hp
        pygame.draw.rect(screen, 'red', (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, 'green', (self.x, self.y, 150*(self.hp/self.max_hp), 20))

class Armor():
    def __init__ (self, x, y, armor, max_armor):
        self.x = x
        self.y = y
        self.armor = armor
        self.max_armor = max_armor

    def draw_bar(self, armor, screen):
        self.armor = armor
        pygame.draw.rect(screen, 'grey', (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, 'blue', (self.x, self.y, 150*(self.armor/self.max_armor), 20))

