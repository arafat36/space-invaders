import pygame.mask
import helpers as fn
from pygame.sprite import DirtySprite
from pygame.rect import Rect
from pygame.surface import Surface
from Settings import Settings


class Bullet(DirtySprite):
    def __init__(self, pos, is_enemy=False):
        super(Bullet, self).__init__()
        self.dirty = 2  # Always dirty => always redrawn

        self.image = fn.get_scaled_image('shot.png', 5)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        # Correct the pos of the bullet depending on who is shooting
        if is_enemy:
            self.rect.midbottom = pos
            self.move_speed = Settings.bullet_dy
        else:
            self.rect.midtop = pos
            self.move_speed = -Settings.bullet_dy


    def update(self):
            self.rect.move_ip(0, self.move_speed)

