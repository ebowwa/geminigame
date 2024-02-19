# utils.py
import pygame

def init_screen():
    pygame.init()
    return pygame.display.set_mode((800, 600))

def init_clock():
    return pygame.time.Clock()

def load_image(file_path, alpha=True):
    image = pygame.image.load(file_path)
    if alpha:
        image = image.convert_alpha()
    return image

def load_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    return sound

def draw_text(surface, text, font, color, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)
