from settings import *
from support import animation_parser




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Placeholder")
        self.running = True


      
    def run_game(self):
        sprite_sheet = animation_parser('Assets/Player/IDLE.png')

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.screen.blit(sprite_sheet)



            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run_game()
    
    



