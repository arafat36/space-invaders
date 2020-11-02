import unittest
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import Mask
from pygame.time import Clock
from space_invaders.Game import Game

class TestGameClass(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()

    
    def hasattr_instance(self, obj, name, _class):
        """Checks if the obj has the named method"""
        return hasattr(obj, name) and isinstance(getattr(obj, name), _class)


    def hasattr_method(self, obj, name):
        """Checks if the obj has the named method"""
        return hasattr(obj, name) and callable(getattr(obj, name))



    ### Attributes ###
    def test_screen(self):
        self.assertTrue(self.hasattr_instance(self.game, "screen", Surface),
                    msg="has screen attr that is Surface instance")
    
    def test_clock(self):
        clock_type = type(Clock())
        self.assertIsInstance(self.game.clock, clock_type,
                    msg="has clock attr that is Clock instance")

    def test_run_game(self):
        self.assertTrue(self.hasattr_method(self.game, "run_game"),
                msg="has run_game method")


if __name__ == '__main__':
    unittest.main()
