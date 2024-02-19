# controls.py
import pygame

class Controls:
    def __init__(self, control_keys):
        self.control_keys = control_keys
        self.pressed_keys = {}

    def update_pressed_keys(self):
        self.pressed_keys = pygame.key.get_pressed()

    def handle_controls(self):
        for key, action in self.control_keys.items():
            if self.pressed_keys[key]:
                action() 