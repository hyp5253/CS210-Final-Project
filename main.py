from settings import *
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Placeholder")
        self.running = True

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.background = pygame.image.load('Assets/Background/Cavern.png')
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT-BOTTOM_PANEL))
        self.screen.fill(COLORS['GREY'])


    def draw_bg(self): self.screen.blit(self.background, (0,0))
      
    def run_game(self):

        knight = Player(250, 420, 300)
        # turn_queue = [knight]
        # action_cooldown = 0
        # action_wait_time = 90

        while self.running:
            self.clock.tick(self.fps)
            self.draw_bg()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
            knight.update('DEATH')
            knight.draw_player(self.screen)

            # if knight.alive == True:
            #     if turn_queue[0] == knight:
            #         turn_queue.append(turn_queue.pop(0))
            #         if action_cooldown >= action_wait_time:
            #             knight.attack()

            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run_game()
    
    



