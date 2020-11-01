# Documentation for Space Invaders

## Classes

The `Game` class is at the highest order. It is the entire game. It manages the interacting object, the sounds, the screen, and the more importantly the logic of the game.

The `Alien`, and `Bullet` classes inherit from `pygame.sprite.Sprite` class. `Aliens`, and `Bullets` inherit from the `pygame.sprite.Group` class, and they can hold multiple `Alien` and `Bullet` instances, respectively. `Ship` inherits instead from `pygame.sprite.GroupSingle`.

There are many benefits with working with Sprites and Groups. All of these four classes have the `update` method. When the `update` method is called on a `Group` object, it invokes the `update` method of all its sprites. The Groups also share the method `draw`, which draws the images of the contained sprites on the given `Surface`.

There are common things between the `Ship`, `Alien`, and `Bullet` object. All of them have the attributes `image`, `rect` and `mask`. These attributes are used to detect collisions, move the objects, and draw them.

Apart from that there are some main differences between the classes.
