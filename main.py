from settings import *
from support import animation_parser
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

        idle_frames = animation_parser('Assets/Player/IDLE.png', 7, 96, 84, 2.5)
        knight = Player(250, 420, 300)

        while self.running:
            self.clock.tick(self.fps)
            self.draw_bg()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
            # self.screen.blit(idle_frames[0], (150, 320))
            knight.update('ATTACK 1')
            knight.draw_player(self.screen)

            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run_game()
    
    



