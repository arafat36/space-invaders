import pygame.mask
import helpers as fn
from pygame.sprite import DirtySprite
from pygame.rect import Rect
from pygame.surface import Surface
from Settings import Settings


class _BaseBullet(DirtySprite):
    def __init__(self):
        super(_BaseBullet, self).__init__()
        self.dirty = 2  # Always dirty => always redrawn

        self.image = fn.get_scaled_image('shot.png', 5)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()


    def update(self):
            self.rect.move_ip(0, self.move_speed)


class PlayerBullet(_BaseBullet):
    def __init__(self, pos):
        super(PlayerBullet, self).__init__()
        self.rect.midtop = pos
        self.move_speed = -Settings.bullet_dy
        self.image.fill(Settings.COLORS['blue'])


class EnemyBullet(_BaseBullet):
    def __init__(self, pos):
        super(PlayerBullet, self).__init__()
        self.rect.midbottom = pos
        self.move_speed = Settings.bullet_dy

    

