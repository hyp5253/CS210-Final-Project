from settings import *

def animation_parser(path, frame_count, frame_w, frame_h, scale):
    sprite_sheet = pygame.image.load(path).convert_alpha()
    frames = [get_frame(sprite_sheet, x, frame_w, frame_h, scale) for x in range(frame_count)]

    return frames

def get_frame(spritesheet, x, frame_w, frame_h, scale):
    frame = pygame.Surface((frame_w, frame_h)).convert_alpha()
    frame.blit(spritesheet, (0,0), ((x * frame_w), 0, frame_w, frame_h))
    frame = pygame.transform.scale(frame, (frame_w*scale, frame_h*scale))
    frame.set_colorkey(COLORS['BLACK'])
    return frame

def draw_title(screen, text, color, x, y):
    text_box = TITLE_FONT.render(text, False, color)
    text_rect = text_box.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_box, text_rect) 

def draw_bg(screen, background): screen.blit(background, (0,0))

    
    