from settings import *

class Button():
    def __init__(self, path, x, y, frame_w, frame_h, scale, text):
        self.button_image = pygame.image.load(path).convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image, (frame_w*scale, frame_h*scale))
        self.rect = self.button_image.get_rect()
        self.rect.center = (x, y)
        self.draw_text(self.button_image, frame_w*scale, frame_h*scale, text)
        self.clicked = False

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

    def draw_text(self, button, button_w, button_h, text): 
        text_rendered = BUTTON_FONT.render(text, False, 'white')
        text_rect = text_rendered.get_rect()
        text_rect.center = (button_w//2, button_h//2)
        button.blit(text_rendered, text_rect)

    

