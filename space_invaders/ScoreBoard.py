import os

from Settings import Settings
from TextSprite import TextSprite


class ScoreBoard:
    """Contains the stats for for the game"""

    def __init__(self):
        self.score = 0
        self.ship_lives = Settings.SHIP_INIT_LIVES
        self.setup_sprites()

    def get_sprites(self):
        self.sprites["ship_lives"].set_text(f"Lives: {self.ship_lives}")
        self.sprites["score"].set_text(f"Score: {self.score}")

        return self.sprites.values()

    def alien_hit(self):
        self.score += Settings.scorepoints["alien_hit"]

    def ship_hit(self):
        self.ship_lives -= 1

    def ship_alien_collision(self):
        self.score += Settings.scorepoints["ship_alien_collision"]
        self.ship_lives -= 1

    def setup_sprites(self):
        self.sprites = {
            "score": TextSprite(f"Score: {self.score}"),
            "ship_lives": TextSprite(f"Lives: {self.ship_lives}"),
        }

        self.sprites["score"].rect.bottomleft = Settings.SCORE_BOTTOMLEFT
        self.sprites["ship_lives"].rect.bottomright = Settings.LIVES_BOTTOMRIGHT

    def at_boss_level(self):
        """
        Prepare ScoreBoard for Boss level.
        """
        self.boss_lives = Settings.BOSS_LIVES
        self.sprites["boss_lives"] = TextSprite(
            f"{self.boss_lives}/{Settings.BOSS_LIVES}"
        )
        self.sprites["boss_lives"].rect.midbottom = Settings.BOSS_LIVES_MIDBOTTOM

    def boss_hit(self):
        self.boss_lives -= 1
        self.sprites["boss_lives"].set_text(f"{self.boss_lives}/{Settings.BOSS_LIVES}")
