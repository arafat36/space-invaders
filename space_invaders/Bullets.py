from pygame.sprite import LayeredDirty

from Settings import Settings


class Bullets(LayeredDirty):
    def __init__(self, screen_width, screen_heigth):
        super(Bullets, self).__init__()
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth

    def update(self, *args, **kwargs):
        # check if bullet is outside the screen
        bullets = []
        for bullet in self.sprites():
            if bullet.rect.left <= 0 or bullet.rect.right >= self.screen_width:
                bullets.append(bullet)
            elif bullet.rect.top <= 0 or bullet.rect.bottom >= self.screen_heigth:
                bullets.append(bullet)
        self.remove(bullets)

        super(Bullets, self).update(*args, **kwargs)  ## Pass on the given arguments...
