from settings import *
from support import animation_parser


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Placeholder")
        self.running = True

      
    def run_game(self):
        frames = animation_parser('Assets/Player/IDLE.png', 84, 84, 2.5)
        

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(frames[len(frames)-1])



            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run_game()
    
    



