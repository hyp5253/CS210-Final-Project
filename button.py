from settings import *

class Button():
    def __init__(self, path, x, y, frame_w, frame_h, scale, text):
        self.button_image = pygame.image.load(path).convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image, (frame_w*scale, frame_h*scale))
        self.rect = self.button_image.get_rect()
        self.rect.center = (x, y)
        self.draw_text(self.button_image, frame_w*scale, frame_h*scale, text)
        self.clicked = False

    def draw_text(self, surface, surface_w, surface_h, text): 
        text_rendered = BUTTON_FONT.render(text, False, 'white')
        text_rect = text_rendered.get_rect()
        text_rect.center = (surface_w//2, surface_h//2)
        surface.blit(text_rendered, text_rect)

    def draw(self, screen): 
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_just_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

            if not pygame.mouse.get_just_pressed()[0]:
                self.clicked = False

        screen.blit(self.button_image, self.rect)
        return action

    

    

