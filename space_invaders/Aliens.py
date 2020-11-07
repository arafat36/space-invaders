from pygame.sprite import LayeredDirty
from Alien import Alien
import time
import helpers as fn
import math


class Aliens(LayeredDirty):
    def __init__(self, screen_width):
        super(Aliens, self).__init__()
        self.screen_width = screen_width
        self.at_edge = False
    
    # Spawns the aliens
    def setup_aliens(self):
        self.empty()

        #alien gap, row and column ammount might have to be calibrated
        alien_gap = 70
        for row in range(6):
            for column in range(7):
                pos = alien_gap + alien_gap * column

                if row <= 1:
                    image1 = fn.get_scaled_image('aliens\\big_alien1.png', 5)
                    image2 = fn.get_scaled_image('aliens\\big_alien2.png', 5)

                elif row <= 3:
                    image1 = fn.get_scaled_image('aliens\\medium_alien1.png', 5)
                    image2 = fn.get_scaled_image('aliens\\medium_alien2.png', 5)

                else:
                    image1 = fn.get_scaled_image('aliens\\small_alien1.png', 5)
                    image2 = fn.get_scaled_image('aliens\\small_alien2.png', 5)

                self.add(Alien((alien_gap + alien_gap * column, 10 + 50 * row), image1, image2))
                            

        self.last_move = time.time()

    def move_aliens(self):
        #check if the aliens are already at the edge (which means they moved down last time and should start to move
        # the other way and not down again) if not check if they have arrived at the edge and move them down
        #otherwise move them sideways
        if not self.at_edge:
            for alien in self.sprites():
                if alien.rect.left <= 10 or alien.rect.right >= self.screen_width - 10:
                    self.at_edge = True
                    break
        
            if self.at_edge:
                for alien in self.sprites():
                    alien.move_down()

            else:
                for alien in self.sprites():
                    alien.move_horizontal()
        
        else:
            for alien in self.sprites():
                    alien.move_horizontal()
                    self.at_edge = False

        self.last_move = time.time()


    def update(self):
        #check if sufficent time has past since last move for them to move again
        if (math.log10(len(self.sprites())) + 0.1) / 4 <= time.time() - self.last_move:
           self.move_aliens()
