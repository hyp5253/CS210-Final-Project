from settings import *

class Skill_Node():
    def __init__(self, path, x, y, left=None, right=None):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.unlocked = True

        self.left = left
        self.right = right

    def draw_skill(self, screen): screen.blit(self.image, self.rect) 


defend   = Skill_Node('Assets/Misc/Iron Shield.png', (SCREEN_WIDTH//6)+130, 600)
attack_3 = Skill_Node('Assets/Misc/Iron Sword.png', (SCREEN_WIDTH//6)+90, 600)
attack_2 = Skill_Node('Assets/Misc/Wooden Sword.png', (SCREEN_WIDTH//6)+54, 600, defend)
attack_1 = Skill_Node('Assets/Misc/Knife.png', (SCREEN_WIDTH//6)+10, 600, attack_2, attack_3)

# add some traversal function to get all of the skills unlocked and display in skill tree area of menu


skill_tree = [attack_1, attack_2, attack_3, defend]

