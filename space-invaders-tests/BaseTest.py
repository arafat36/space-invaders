import unittest

class BaseTest:

    def hasattr_instance(self, obj, name, _class):
        """Checks if the obj has the named attr from given class"""
        return hasattr(obj, name) and isinstance(getattr(obj, name), _class)


    def hasattr_method(self, obj, name):
        """Checks if the obj has the named method"""
        return hasattr(obj, name) and callable(getattr(obj, name))


    def test_ship_super(self):
        self.assertTrue(issubclass(Ship, DirtySprite), msg="Ship inherits from GroupSingle class")
    

    def test_class_super(self):
        raise NotImplementedError


    def test_class_attributes(self):
        raise NotImplementedError


    def test_class_methods(self):
        raise NotImplementedError