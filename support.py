from settings import *

def animation_parser(path, frame_w, frame_h, scale):
    sprite_sheet = pygame.image.load(path).convert_alpha()
    frame_count = sprite_sheet.get_width() // sprite_sheet.get_height()
    frames = [get_frame(sprite_sheet, x, frame_w, frame_h, scale) for x in range(frame_count)]

    return frames

def get_frame(spritesheet, x, frame_w, frame_h, scale):
    frame = pygame.Surface((frame_w, frame_h)).convert_alpha()
    frame.blit(spritesheet, (0,0), ((x * frame_w), 0, frame_w, frame_h))
    frame = pygame.transform.scale(frame, (frame_w*scale, frame_h*scale))
    # frame.set_colorkey(color)
    return frame

    
    