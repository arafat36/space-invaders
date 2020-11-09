from pygame.sprite import DirtySprite
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import from_surface 
from Settings import Settings

class Alien(DirtySprite):
    def __init__(self, pos, image1, image2):
        super(Alien, self).__init__()
        self.dirty = 2

        self.image = image1
        self.rect = self.image.get_rect()
        self.mask = from_surface(image1)
        self.rect.center = pos
        self.move_speed_x = Settings.alien_dx
        self.move_speed_y = Settings.alien_dy
        self.direction = 1
        self.images = {1:image1, -1:image2}
        self.current_image_number = 1

    def move_horizontal(self):
        self.rect.move_ip(self.move_speed_x * self.direction, 0)
        self.current_image_number = -self.current_image_number
        self.image = self.images[self.current_image_number]

    def move_down(self):
        self.rect.move_ip(0, self.move_speed_y)
        self.direction = -self.direction
        self.current_image_number = -self.current_image_number
        self.image = self.images[self.current_image_number]

    def get_center(self):
        return self.rect.center

    
class BossAlien():
    """ """
    pass
