import os

import pygame.mask
from pygame.rect import Rect
from pygame.sprite import DirtySprite
from pygame.surface import Surface

import helpers as fn
from Settings import Settings


class _BaseBullet(DirtySprite):
    def __init__(self):
        super(_BaseBullet, self).__init__()
        self.dirty = 2  # Always dirty => always redrawn

        _image_path = os.path.join(Settings.IMAGES_DIR, "shot.png")
        self.image = fn.get_scaled_image(_image_path, 5)

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()

        self.move_speed = Settings.bullet_dy

    def update(self):
        raise NotImplementedError


class PlayerBullet(_BaseBullet):
    def __init__(self, pos):
        super(PlayerBullet, self).__init__()
        self.rect.midtop = pos
        self.image.fill(Settings.COLORS["blue"])

    def update(self, *args, **kwargs):
        self.rect.move_ip(0, -self.move_speed)


class EnemyBullet(_BaseBullet):
    def __init__(self, pos):
        super(EnemyBullet, self).__init__()
        self.rect.midbottom = pos
        self.image.fill(Settings.COLORS["red"])

    def update(self, *args, **kwargs):
        self.rect.move_ip(0, self.move_speed)


class BossBullet(EnemyBullet):
    def __init__(self, pos, ship_center):
        super(BossBullet, self).__init__(pos)
        self.dy = self.move_speed
        # self.dx = self.get_accurate_dx(ship_center)
        self.dx = 0
        self.image.fill((255, 0, 0))
        self.latency = Settings.bossbullet_latency

    def get_accurate_dx(self, ship_center):
        ship_x, ship_y = ship_center
        bullet_x, bullet_y = self.rect.x, self.rect.y
        delta_x, delta_y = (bullet_x - ship_x), (bullet_y - ship_y)

        try:
            return delta_x * self.dy / delta_y
        except ZeroDivisionError:
            return 0

    def update(self, ship_center):
        diff_dx = self.dx - self.get_accurate_dx(ship_center)

        if diff_dx > 0:
            self.dx -= self.latency
        if diff_dx < 0:
            self.dx += self.latency

        self.rect.move_ip(self.dx, self.dy)
