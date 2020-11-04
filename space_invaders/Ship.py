from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import Mask
from pygame.sprite import GroupSingle, Sprite

class Ship(GroupSingle):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = Surface((100, 50))
        self.rect = self.image.get_rect()
        self.mask = Mask((self.image.get_width(), self.image.get_height()))
        self.sprite = Sprite(self)

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