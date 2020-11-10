import random
import sys

import pygame as pg
import pygame.locals as pgloc
import pygame.sprite as sprite
from pygame.sprite import LayeredDirty

from Alien import BossAlien
from Aliens import Aliens
from Bullet import BossBullet, EnemyBullet, PlayerBullet
from Bullets import Bullets
from GameSounds import GameSounds
from ScoreBoard import ScoreBoard
from Settings import Settings
from Ship import Ship
from TextSprite import TextSprite


class Game:
    """
    Represents the Space Invaders Game
    """

    def __init__(self):
        """
        Initializes a Game instance
        """
        # Initialize pygame module
        pg.init()

        # Initialize display screen
        self.width = Settings.D_WIDTH
        self.height = Settings.D_HEIGHT

        pg.display.set_caption(Settings.D_CAPTION)
        # pg.display.set_icon(surface)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.bgd = pg.Surface(self.screen.get_size())
        self.bgd.fill(Settings.COLORS["black"])

        # Initialize Game Sounds
        self.sounds = GameSounds()

        # Initialize a Clock instance
        self.clock = pg.time.Clock()

        # Initialize Game elements
        self.ship = Ship(Settings.SHIP_START_POS)
        self.player_bullets = Bullets(self.width, self.height)
        self.enemy_bullets = Bullets(self.width, self.height)
        self.aliens = Aliens(self.width)
        self.scoreboard = ScoreBoard()

        self.layered_sprites = LayeredDirty()  # Used for blitting to screen

    def run_game(self):
        """
        Runs the Game
        """
        self.playing = False
        self.has_won = False
        self.at_bosslevel = False

        while True:
            #  Wait for user to begin
            self.start_screen()

            while self.playing:
                # Check for events, and respond accordingly
                self.handle_events()

                # Check collisions, and move aliens and bullets
                self.update_states()

                # Put changes on display
                self.update_display()

                # Keep the FPS constant on all machines
                self.clock.tick(Settings.FPS)

            # Game ended, show outcome
            self.end_screen()

    def handle_events(self):
        """
        Handles the events in the game
        """
        # Get all the state of keys
        pressed = pg.key.get_pressed()

        # Check if the left (or a), right (or d), or spacebar are pressed
        to_left = pressed[pgloc.K_LEFT] or pressed[pgloc.K_a]
        to_right = pressed[pgloc.K_RIGHT] or pressed[pgloc.K_d]

        # Handle the keypresses
        if to_left:
            if self.ship.get_left() > 0:
                self.ship.move_left()

        if to_right:
            if self.ship.get_right() < self.width:
                self.ship.move_right()

        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # Check if spacebar is pressed
            elif event.type == pg.KEYDOWN:
                if event.key == pgloc.K_SPACE:
                    if len(self.player_bullets) < Settings.ship_bullet_limit:
                        bullet_pos = self.ship.get_center()
                        bullet_obj = PlayerBullet(bullet_pos)
                        self.player_bullets.add(bullet_obj)

                        self.sounds.bullet_shot()

                elif event.key == pgloc.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update_states(self):
        """
        Update and handle the states of the Ship, Aliens and Bullets
        """
        # Check if game over
        self.check_gameover()

        # Enemy bullets hitting player
        self.handle_ship_hit()

        if not self.at_bosslevel:
            # Player bullets hitting aliens
            self.handle_aliens_hit()

            # Alien-ship collision
            self.handle_ship_alien_collision()

            # Random aliens shooting bullets
            self.random_alien_shots()

            if len(self.aliens) == 0:
                self.init_boss_level()

            # Move the bullets and aliens
            for group in (self.aliens, self.enemy_bullets, self.player_bullets):
                group.update()

        else:
            # Player bullets hitting aliens
            self.handle_boss_hit()

            # Random aliens shooting bullets
            self.random_boss_shot()

            # Move the bullets
            self.player_bullets.update()

            # Enemy bullets are like missiles...
            self.enemy_bullets.update(self.ship.get_center())

            # ...and boss alien
            self.boss_alien.update()

    def update_display(self):
        """
        Updates the display, ie. makes the changes visible to the user.

        To boost performance, it erases specific locations (of the aliens, bullets etc.)
        and updates only those areas.
        """

        all_sprites = [
            *self.enemy_bullets.sprites(),
            *self.player_bullets.sprites(),
            *self.scoreboard.get_sprites(),
            self.ship,
        ]

        if not self.at_bosslevel:
            all_sprites.extend(self.aliens.sprites())
        else:
            all_sprites.append(self.boss_alien)

        self.layered_sprites.empty()
        for s in all_sprites:
            self.layered_sprites.add(s)

        self.layered_sprites.clear(self.screen, self.bgd)
        rect_list = self.layered_sprites.draw(self.screen)

        pg.display.update(rect_list)

    def handle_aliens_hit(self):
        """
        Deletes the hit aliens and the used bullets.
        For each hit alien, play sound effect and update score.
        """
        aliens_hit = sprite.groupcollide(
            self.player_bullets, self.aliens, True, True, sprite.collide_mask
        )
        for __ in aliens_hit:
            self.scoreboard.alien_hit()
            self.sounds.alien_hit()

    def handle_ship_hit(self):
        """
        Deletes the bullets that hit the ship, and plays sound effect and update lives.
        """
        ship_hit = sprite.spritecollide(
            self.ship, self.enemy_bullets, True, sprite.collide_mask
        )
        if ship_hit:
            self.scoreboard.ship_hit()
            self.sounds.ship_hit()
            # self.aliens.setup_aliens()

    def handle_ship_alien_collision(self):
        """
        If alien and ship collided, play sound and update lives.
        """
        ship_alien_collision = sprite.spritecollideany(self.ship, self.aliens)
        if ship_alien_collision:
            self.scoreboard.ship_alien_collision()
            self.sounds.ship_alien_collision()
            self.aliens.setup_aliens()

    def random_alien_shots(self):
        """
        If the are aliens, make random ones shoot a number of bullets.
        """
        if len(self.aliens):
            while len(self.enemy_bullets) < Settings.alien_bullet_limit:
                _random_idx = random.randint(0, len(self.aliens) - 1)
                shooting_alien = self.aliens.get_sprite(_random_idx)
                bullet_pos = shooting_alien.get_center()
                bullet_obj = EnemyBullet(bullet_pos)
                self.enemy_bullets.add(bullet_obj)

                self.sounds.bullet_shot()

    def check_gameover(self):
        """
        Check if the game is over.
        The game is over if the number of lives in scoreboard is 0.
        """
        if self.scoreboard.ship_lives == 0:
            self.playing = False

        elif self.at_bosslevel:
            if self.scoreboard.boss_lives == 0:
                self.sounds.boss_dead()
                self.playing = False
                self.has_won = True

    def init_boss_level(self):
        self.at_bosslevel = True
        self.boss_alien = BossAlien(self.width, self.height)
        Settings.alien_bullet_limit = 1
        Settings.ship_bullet_limit = 1
        Settings.ship_dx *= 1.5
        self.scoreboard.at_boss_level()

    def handle_boss_hit(self):
        """
        Deletes the bullets that hit the boss, and plays sound effect and update lives.
        """
        boss_hit = sprite.spritecollide(
            self.boss_alien, self.player_bullets, True, sprite.collide_mask
        )
        if boss_hit:
            self.scoreboard.boss_hit()
            self.sounds.boss_hit()

    def random_boss_shot(self):
        if len(self.enemy_bullets) < Settings.alien_bullet_limit:
            bullet_pos = self.boss_alien.get_center()
            bullet_obj = BossBullet(bullet_pos, self.ship.get_center())
            self.enemy_bullets.add(bullet_obj)

            self.sounds.bullet_shot()

    def start_screen(self):
        # Create Text Sprites
        _sprite1 = TextSprite(Settings.START_SCREEN_TEXT_1)
        _sprite2 = TextSprite(Settings.INSTRUCTION_TEXT)
        # Position them
        _sprite1.rect.midbottom = (
            self.width // 2,
            (self.height - Settings.D_PADDING) // 2,
        )
        _sprite2.rect.midtop = (
            self.width // 2,
            (self.height + Settings.D_PADDING) // 2,
        )

        # And blit them to screen
        self.layered_sprites.add(_sprite1, _sprite2)
        self.layered_sprites.draw(self.screen)
        pg.display.flip()

        while not self.playing:
            # Handle events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit_game()

                # Check if Enter is pressed
                elif event.type == pg.KEYDOWN:
                    if event.key == pgloc.K_ESCAPE:
                        self.exit_game()

                    elif event.key == pgloc.K_RETURN:
                        self.playing = True

    def end_screen(self):
        self.screen.fill(Settings.COLORS["black"])

        if self.has_won:
            _sprite1 = TextSprite(Settings.WON_SCREEN_TEXT)
        else:
            _sprite1 = TextSprite(Settings.LOST_SCREEN_TEXT)

        # Position them
        _sprite1.rect.midbottom = (
            self.width // 2,
            (self.height - Settings.D_PADDING) // 2,
        )

        # And blit them to screen
        self.screen.blit(_sprite1.image, _sprite1.rect)
        pg.display.flip()

        while not self.playing:
            # Handle events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit_game()

                # Check if Enter is pressed
                elif event.type == pg.KEYDOWN:
                    if event.key == pgloc.K_ESCAPE:
                        self.exit_game()

    def exit_game(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
