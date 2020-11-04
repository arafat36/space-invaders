from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import Mask

class Bullet(Sprite):
    def __init__(self, pos, enemy = False):
        super(Bullet, self).__init__()
        self.image = Surface((5, 20))
        self.rect = self.image.get_rect()
        self.mask = Mask((self.image.get_width(), self.image.get_height()))
        self.enemy = enemy
        self.rect.center = pos
        self.move_speed = 15

    def update(self):
        if self.enemy:
            self.rect.move_ip(0, self.move_speed)

        if not self.enemy:
            self.rect.move_ip(0, -self.move_speed)

