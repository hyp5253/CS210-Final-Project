from settings import *

class Skill_Node():
    def __init__(self, path, x, y, left=None, right=None):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.unlocked = False

        self.left = left
        self.right = right

    def draw_skill(self, screen): screen.blit(self.image, self.rect) 


defend   = Skill_Node('Assets/Misc/Iron Shield.png', (SCREEN_WIDTH//6)+130, 600)
attack_3 = Skill_Node('Assets/Misc/Iron Sword.png', (SCREEN_WIDTH//6)+90, 600)
attack_2 = Skill_Node('Assets/Misc/Wooden Sword.png', (SCREEN_WIDTH//6)+54, 600, defend)
attack_1 = Skill_Node('Assets/Misc/Knife.png', (SCREEN_WIDTH//6)+10, 600, attack_2, attack_3)

attack_1.unlocked = True

def breadth_first_traversal(root, screen):
   if not root: return root

   queue = [root]
   while len(queue) > 0:
      curr = queue.pop(0)
      if curr.unlocked: curr.draw_skill(screen)
      
      if curr.left: queue.append(curr.left)
      if curr.right: queue.append(curr.right)

