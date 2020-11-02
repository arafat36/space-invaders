import unittest
from space_invaders.Ship import Ship
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.mask import Mask
from pygame.sprite import GroupSingle, Sprite

class TestShipClass(unittest.TestCase):

    def test_ship_super(self):
        self.assertTrue(issubclass(Ship, GroupSingle), msg="Ship inherits from GroupSingle class")
    

class TestShipAttributes(unittest.TestCase):

    def setUp(self):
        self.ship = Ship()

    
    def hasattr_instance(self, obj, name, _class):
        """Checks if the obj has the named attr from given class"""
        return hasattr(obj, name) and isinstance(getattr(obj, name), _class)

    ### Attributes ###
    def test_rect(self):
        self.assertTrue(self.hasattr_instance(self.ship, "rect", Rect),
                    msg="has rect attr that is Rect instance")

    def test_image(self):
        # self.assertTrue(hasattr(self.ship, "image"), msg="has image attr"))
        # self.assertTrue(isinstance(self.ship.image, Surface), msg="image attr is Surface instance")
        self.assertTrue(self.hasattr_instance(self.ship, "image", Surface),
                    msg="has image attr that is Surface instance")

    def test_mask(self):
        mask_type = Mask((0,0))
        self.assertTrue(self.hasattr_instance(self.ship, "mask", mask_type),
                    msg="has mask attr that is Mask instance")

    def test_sprite(self):
        self.assertTrue(self.hasattr_instance(self.ship, "sprite", Sprite),
                    msg="has sprite attr that is Sprite instance")


class TestShipMethods(unittest.TestCase):

    def setUp(self):
        self.ship = Ship()

    def hasattr_method(self, obj, name):
        """Checks if the obj has the named method"""
        return hasattr(obj, name) and callable(getattr(obj, name))

    ### Methods ###
    def test_get_center(self):
        self.assertTrue(self.hasattr_method(self.ship, "get_center"),
                    msg="has get_center method")

    def test_get_left(self):
        self.assertTrue(self.hasattr_method(self.ship, "get_left"),
                    msg="has get_left method")

    def test_get_right(self):
        self.assertTrue(self.hasattr_method(self.ship, "get_right"),
                    msg="has get_right method")
    

    def test_move_left(self):
        self.assertTrue(self.hasattr_method(self.ship, "move_left"),
                    msg="has move_left method")

    def test_move_right(self):
        self.assertTrue(self.hasattr_method(self.ship, "move_right"),
                     msg="has move_right method")


if __name__ == '__main__':
    unittest.main()
