import os

from pygame.mixer import Sound

from Settings import Settings


class GameSounds:
    """Contains the sound effects for the game"""

    def __init__(self):
        self._alien_hit = Sound(os.path.join(Settings.SOUNDS_DIR, "explosion.wav"))
        self._ship_hit = Sound(os.path.join(Settings.SOUNDS_DIR, "playerhurt_1.wav"))
        self._bullet_shot = Sound(os.path.join(Settings.SOUNDS_DIR, "a-shot.wav"))
        self._ship_alien_collision = Sound(
            os.path.join(Settings.SOUNDS_DIR, "playerhurt_1.wav")
        )
        self._boss_hit = Sound(os.path.join(Settings.SOUNDS_DIR, "explosion.wav"))
        self._boss_dead = Sound(
            os.path.join(Settings.SOUNDS_DIR, "screams-in-pain.wav")
        )

        self._bullet_shot.set_volume(0.55)

    def alien_hit(self):
        self._alien_hit.play()

    def ship_hit(self):
        self._ship_hit.play()

    def ship_alien_collision(self):
        self._ship_alien_collision.play()

    def bullet_shot(self):
        self._bullet_shot.play()

    def boss_hit(self):
        self._boss_hit.play()

    def boss_dead(self):
        self._boss_dead.play()
