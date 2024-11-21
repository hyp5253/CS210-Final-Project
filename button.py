from settings import *

class Button():
    def __init__(self, path, x, y, frame_w, frame_h, scale, text):
        self.button_image = pygame.image.load(path).convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image, (frame_w*scale, frame_h*scale))
        self.rect = self.button_image.get_rect()
        self.rect.center = (x, y)
        self.draw_text(self.button_image, frame_w*scale, frame_h*scale, text)

    def draw(self, screen): 
        screen.blit(self.button_image, self.rect)

    def draw_text(self, button, button_w, button_h, text): 
        text_rendered = BUTTON_FONT.render(text, False, 'white')
        text_rect = text_rendered.get_rect()
        text_rect.center = (button_w//2, button_h//2)
        button.blit(text_rendered, text_rect)

    

