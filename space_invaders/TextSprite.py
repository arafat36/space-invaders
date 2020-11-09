from Settings import Settings
from pygame.font import Font
from pygame.sprite import DirtySprite

class TextSprite(DirtySprite):
    """Creates a sprite with text"""
    def __init__(self, initText=""):
        super(TextSprite, self).__init__()
        self.dirty = 2
        self.font = Font(Settings.SCOREBOARD_FONT_PATH, 18)
        self.image = self.font.render(initText, False, Settings.COLORS['white'], Settings.COLORS['black'])
        self.rect = self.image.get_rect()


    def set_text(self, text):
        self.image = self.font.render(text, False, Settings.COLORS['white'], Settings.COLORS['black'])
        # self.rect = self.image.get_rect()  # Creates bug
