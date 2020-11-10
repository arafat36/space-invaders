from pygame.sprite import DirtySprite
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import from_surface 
from Settings import Settings
from os.path import join as path_join
import helpers as fn
import time

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

    
class BossAlien(DirtySprite):
    def __init__(self, screen_width, screen_height):
        super(BossAlien, self).__init__()
        self.dirty = 2
        self.images = self.get_images()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.rect.center = (screen_width // 2, 0 - self.rect.height // 2)
        self.target_pos_y = self.rect.height // 2
        self.move_speed = 3
        self.current_image = 0
        self.animation_speed = 0.3
        self.last_image_change = time.time()

    def get_images(self):
        aliens_path = path_join(Settings.IMAGES_DIR, "aliens")
        return {0:fn.get_scaled_image(path_join(aliens_path, "boss1.png"), 5),
        1:fn.get_scaled_image(path_join(aliens_path, "boss2.png"), 5),
        2:fn.get_scaled_image(path_join(aliens_path, "boss3.png"), 5),
        3:fn.get_scaled_image(path_join(aliens_path, "boss4.png"), 5)}

    def animate(self):
        if self.animation_speed < time.time() - self.last_image_change:
            if self.current_image < 3:
                self.current_image += 1
            else:
                self.current_image = 0

            self.image = self.images[self.current_image]
            self.last_image_change = time.time()

    def move(self):
        if self.rect.centery != self.target_pos_y:
            if self.rect.centery < self.target_pos_y - self.move_speed:
                self.rect.move_ip(0, self.move_speed)
            else:
                self.rect.centery = self.target_pos_y

    def update(self):
        self.move()
        self.animate()




