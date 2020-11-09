import os
from Settings import Settings
from TextSprite import TextSprite

class ScoreBoard:
    """Contains the stats for for the game"""
    def __init__(self):
        self.score = 0
        self.lives = Settings.SHIP_INIT_LIVES
        self.setup_sprites()

    def get_sprites(self):
        self.sprites['lives'].set_text(f'Lives: {self.lives}')
        self.sprites['score'].set_text(f'Score: {self.score}')

        return self.sprites.values()


    def alien_hit(self):
        self.score += Settings.scorepoints["alien_hit"]


    def ship_hit(self):
        self.lives -= 1
        

    def ship_alien_collision(self):
        self.score += Settings.scorepoints["ship_alien_collision"]
        self.lives -= 1


    def setup_sprites(self):
        self.sprites = {
            "score": TextSprite(f'Score: {self.score}'),
            "lives": TextSprite(f'Lives: {self.lives}')
        }

        self.sprites["score"].rect.bottomleft = Settings.SCORE_BOTTOMLEFT
        self.sprites["lives"].rect.bottomright = Settings.LIVES_BOTTOMRIGHT

