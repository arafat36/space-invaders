import pygame.image
import os

class Settings:

    ###### File folders ######
    # File path should work no matter the OS
    IMAGES_DIR = os.path.join("..", "images")
    SOUNDS_DIR = os.path.join("..", "sounds")

    ###### Display settings ######
    D_WIDTH = 512 + 128
    D_HEIGHT = 1024 - 256
    D_PADDING = 20
    D_CAPTION = "Space Invaders - The ULTIMATE VERSION"
    # D_ICON = pygame.image.load()
    FPS = 60


    ###### Colors ######
    COLORS = {
        'black': (0, 0, 0),
        'blue': (0, 0, 255),
        'red': (255, 0, 0)
    }


    ###### Bullet settings ######
    bullet_dy = 12


    ###### Ship settings ######
    ship_dx = 10
    SHIP_START_POS = (D_WIDTH // 2, D_HEIGHT - D_PADDING)


    ###### ScoreBoard settings ######


