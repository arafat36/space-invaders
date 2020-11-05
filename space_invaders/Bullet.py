from pygame.sprite import DirtySprite
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import from_surface

class Bullet(DirtySprite):
    def __init__(self, pos, enemy = False):
        super(Bullet, self).__init__()
        self.dirty = 2

        self.image = Surface((5, 20))
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.enemy = enemy
        self.rect.center = pos
        self.move_speed = 15

    def update(self):
        if self.enemy:
            self.rect.move_ip(0, self.move_speed)

        if not self.enemy:
            self.rect.move_ip(0, -self.move_speed)

