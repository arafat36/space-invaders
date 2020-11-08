import os
import pygame.mask
import helpers as fn
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sprite import DirtySprite
from Settings import Settings

class Ship(DirtySprite):
    def __init__(self, midbottom):
        super(Ship, self).__init__()
        
        self.dirty = 2  # Always dirty => always redrawn
        _image_path = os.path.join(Settings.IMAGES_DIR, "ship.png")
        self.image = fn.get_scaled_image(_image_path, 5)

        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom

        self.mask = pygame.mask.from_surface(self.image)

        self.move_speed = 10

    
    def get_center(self):
        return self.rect.center

    def get_left(self):
        return self.rect.left

    def get_right(self):
        return self.rect.right

    def move_left(self):
        self.rect.move_ip(-self.move_speed, 0)

    def move_right(self):
        self.rect.move_ip(self.move_speed, 0)