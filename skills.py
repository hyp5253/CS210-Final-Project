from settings import *
from entity import Knight

class Skill_Node():
    def __init__(self, path, x, y, left=None, right=None):
        self.icon = pygame.image.load('Assets/UI/Action Border.png')
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (x, y)

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.equipped = False
        self.left = left
        self.right = right

    def draw_skill(self, screen): 
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.image, self.rect) 

iron_shield   = Skill_Node('Assets/Misc/Iron Shield.png', (SCREEN_WIDTH//6)+100, 600)
wooden_shield   = Skill_Node('Assets/Misc/Wooden Shield.png', (SCREEN_WIDTH//6)+100, 600, iron_shield)
iron_sword = Skill_Node('Assets/Misc/Iron Sword.png', (SCREEN_WIDTH//6)+30, 600)
wooden_sword = Skill_Node('Assets/Misc/Wooden Sword.png', (SCREEN_WIDTH//6)+30, 600, iron_sword)
knife = Skill_Node('Assets/Misc/Knife.png', (SCREEN_WIDTH//6)+30, 600, wooden_sword, wooden_shield)
heal = Skill_Node('Assets/Misc/Heart.png', (SCREEN_WIDTH//6)+170, 600)


wooden_shield.equipped = True
knife.equipped = True

def breadth_first_traversal(root, screen):
   if not root: return root

   queue = [root]
   while len(queue) > 0:
      curr = queue.pop(0)
      if curr.equipped: curr.draw_skill(screen)
      
      if curr.left: queue.append(curr.left)
      if curr.right: queue.append(curr.right)

