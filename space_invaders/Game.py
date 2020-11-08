import sys
import random
import pygame as pg
import pygame.locals as pgloc
import pygame.sprite as sprite

from pygame.sprite import LayeredDirty

from Settings import Settings
from Ship import Ship
from Bullet import PlayerBullet, EnemyBullet
from Bullets import Bullets
from Aliens import Aliens

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
        self.bgd.fill(Settings.COLORS['black'])

        # Initialize Game Sounds
        # self.sounds = GameSounds()

        # Initialize a Clock instance
        self.clock = pg.time.Clock()

        # Initialize Game elements
        self.ship = Ship(Settings.SHIP_START_POS)
        self.player_bullets = Bullets(self.width, self.height)
        self.enemy_bullets = Bullets(self.width, self.height)
        self.aliens = Aliens(self.width)
        # self.score_board = ScoreBoard()

        self.layered_sprites = LayeredDirty()  # Used for blitting to screen
       

    def run_game(self):
        """
        Runs the Game
        """
        
        while True:
            # Check for events, and respond accordingly 
            self.handle_events()

            # Check collisions, and move aliens and bullets
            self.update_states()

            # Put changes on display
            self.update_display()

            # Keep the FPS constant on all machines
            self.clock.tick(Settings.FPS)


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
                    bullet_pos = self.ship.get_center()
                    bullet_obj = PlayerBullet(bullet_pos)
                    self.player_bullets.add(bullet_obj)

                elif event.key == pgloc.K_ESCAPE:
                    pg.quit()
                    sys.exit()


    def update_states(self):
        """
        Update and handle the states of the Aliens and the Bullets
        """
        # # Check for collisions

        # Player bullets hitting aliens
        aliens_hit = sprite.groupcollide(self.player_bullets, self.aliens, True, True, sprite.collide_mask)
        # for __ in aliens_hit:
        #     self.scoreboard.alien_hit()
        #     self.sounds.alien_hit()

        # Enemy bullets hitting player
        ship_hit = sprite.spritecollideany(self.ship, self.enemy_bullets)
        if ship_hit:
            # self.score_board.ship_hit()
            # self.sounds.ship_hit()
            # self.aliens.at_top()
            print("Hit by  enemy!")
              

        # # Alien-ship collision
        # ship_alien_collision = sprite.spritecollideany(self.ship.sprite, self.aliens)
        # if ship_alien_collision:
        #     self.score_board.ship_alien_collision()
        #     self.sounds.ship_alien_collision()
        #     self.aliens.at_top()


        # Random aliens shooting bullets
        if len(self.aliens):
            while len(self.enemy_bullets) < 2:
                _random_idx = random.randint(0, len(self.aliens) - 1)
                shooting_alien = self.aliens.get_sprite(_random_idx)
                bullet_pos = shooting_alien.get_center()
                bullet_obj = EnemyBullet(bullet_pos)
                self.enemy_bullets.add(bullet_obj)


        # Move the bullets and aliens
        for group in (self.aliens, self.enemy_bullets, self.player_bullets):
            group.update()


    def update_display(self):
        """
        Updates the display, ie. makes the changes visible to the user.

        To boost performance, it erases specific locations (of the aliens, bullets etc.) 
        and updates only those areas.
        """
        
        all_sprites = (
            *self.enemy_bullets.sprites(),
            *self.player_bullets.sprites(),
            *self.aliens.sprites(),
            self.ship
        )

        self.layered_sprites.empty()
        for s in all_sprites:
            self.layered_sprites.add(s)

        self.layered_sprites.clear(self.screen, self.bgd)
        rect_list = self.layered_sprites.draw(self.screen)

        pg.display.update(rect_list)


if __name__ == '__main__':
    game = Game()
    game.run_game()