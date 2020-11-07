from pygame.sprite import LayeredDirty
from Settings import Settings

class Bullets(LayeredDirty):
    def __init__(self):
        super(Bullets, self).__init__()
    
    
    def update(self):
        # TODO - Dom bullets som går förbi skärmen ska dö
        # - gäller sidled och höjdled
        # ...
        super(Bullets, self).update()


