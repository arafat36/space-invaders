from pygame.sprite import LayeredDirty
from Settings import Settings

class Bullets(LayeredDirty):
    def __init__(self):
        super(Bullets, self).__init__()
    

    def update(self):
        # TODO - Dom bullets som går förbi skärmen ska dö
        # Kolla om bullet ärver från PlyerBullet, eller EnemyBullet klassen
        # Och sen kolla om den åker underifrån eller uppifrån... 
        super(Bullets, self).update()


