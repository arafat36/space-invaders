import sys
import random
import pygame as pg
import pygame.locals as pgloc
import pygame.sprite as sprite

from pygame.sprite import LayeredDirty

from Ship import Ship
from Bullet import Bullet
from Bullets import Bullets

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
        self.width = 1024
        self.height = 512
        pg.display.set_caption("Space Invaders - The ULTIMATE VERSION")
        # pg.display.set_icon(surface)
        self.screen = pg.display.set_mode((self.width, self.height))
        self.bgd = pg.Surface(self.screen.get_size())
        BLACK = (0, 0, 0)
        self.bgd.fill(BLACK)

        # Initialize Game Sounds
        # self.sounds = GameSounds()

        # Initialize a Clock instance
        self.clock = pg.time.Clock()

        # Initialize Game elements
        self.ship = Ship((self.width // 2, self.height - 30))
        self.ship_group = LayeredDirty(self.ship)
        self.player_bullets = Bullets()
        # self.enemy_bullets = Bullets()
        # self.aliens = Aliens()
        # self.score_board = ScoreBoard()
        # self.groups = (self.aliens, self.enemy_bullets, self.player_bullets)
        self.groups = (self.player_bullets,)
       

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
            self.clock.tick(60)


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
            # print("Keydown LEFT")

        if to_right:
            if self.ship.get_right() < self.width:
                self.ship.move_right()
            # print("Keydown RIGHT")


        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            # Check if spacebar is pressed
            elif event.type == pg.KEYDOWN:
                if event.key == pgloc.K_SPACE:
                    bullet_pos = self.ship.get_center()
                    # bullet_pos = self.ship.get_center()
                    bullet_obj = Bullet(bullet_pos)
                    self.player_bullets.add(bullet_obj)

                    # print("Keydown SPACE")
                    # pass


    def update_states(self):
        """
        Update and handle the states of the Aliens and the Bullets
        """
        pass 
        # # Check for collisions

        # # Player bullets hitting aliens
        # aliens_hit = sprite.groupcollide(self.player_bullets, self.aliens, True, True, sprite.collide_mask)
        # for __ in aliens_hit:
        #     self.scoreboard.alien_hit()
        #     self.sounds.alien_hit()

        # # Enemy bullets hitting player
        # ship_hit = sprite.spritecollideany(self.ship, self.enemy_bullets)
        # if ship_hit:
        #     self.score_board.ship_hit()
        #     self.sounds.ship_hit()
        #     self.aliens.at_top()
              

        # # Alien-ship collision
        # ship_alien_collision = sprite.spritecollideany(self.ship.sprite, self.aliens)
        # if ship_alien_collision:
        #     self.score_board.ship_alien_collision()
        #     self.sounds.ship_alien_collision()
        #     self.aliens.at_top()


        # # Random aliens shooting bullets
        # while len(self.aliens) < 3:
        #     shooting_alien = random.choice(self.aliens)
        #     bullet_pos = shooting_alien.center
        #     bullet_obj = Bullet(bullet_pos, enemy=True)
        #     self.enemy_bullets.add(bullet_obj)


        # Move the bullets and aliens
        for group in self.groups:
            group.update()


    def update_display(self):
        """
        Updates the display, ie. makes the changes visible to the user.

        To boost performance, it erases specific locations (of the aliens, bullets etc.) 
        and updates only those areas.
        """
        #Track the changed areas of the screen
        changed_areas = list()

        # Erase the bullets and aliens
        for group in self.groups:
            print(group)
            group.clear(self.screen, self.bgd)

        # Draw new content
        for group in self.groups:
            rect_list = group.draw(self.screen)
            changed_areas.extend(rect_list)

        # Erase and redraw the ship
        self.ship_group.clear(self.screen, self.bgd)
        rect_list = self.ship_group.draw(self.screen)
        changed_areas.extend(rect_list)

        
        # Push it to the display window
        # print(changed_areas)
        pg.display.update(changed_areas)
        # pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()