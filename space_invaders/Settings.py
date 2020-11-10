import os

import pygame.image


class Settings:

    ###### File folders ######
    # File path should work no matter the OS
    IMAGES_DIR = os.path.join("..", "images")
    SOUNDS_DIR = os.path.join("..", "sounds")
    FONTS_DIR = os.path.join("..", "fonts")

    ###### Display settings ######
    D_WIDTH = 512 + 256
    D_HEIGHT = 1024 - 256
    D_PADDING = 20
    D_CAPTION = "Space Invaders - The ULTIMATE VERSION"
    # D_ICON = pygame.image.load()
    FPS = 60

    START_SCREEN_TEXT_1 = "Space Invaders - ULTIMATE VERSION"

    INSTRUCTION_TEXT = "(Press Enter to start, Esc to exit)"

    WON_SCREEN_TEXT = "CONGRATULATIONS, YOU WON THE GAME!"
    LOST_SCREEN_TEXT = " GAME OVER, YOU LOST..."

    ###### Colors ######
    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
    }

    ###### Bullet settings ######
    bullet_dy = 12
    bossbullet_latency = 0.5  # less means higher latency

    ###### Ship settings ######
    ship_dx = 10
    SHIP_START_POS = (D_WIDTH // 2, D_HEIGHT - 60)  # 60 should give space to scoreboard
    ship_bullet_limit = 4
    SHIP_INIT_LIVES = 5

    ###### Alien settings ######
    alien_dx = 20
    alien_dy = 30
    alien_bullet_limit = 2

    BOSS_LIVES = 10

    ###### ScoreBoard settings ######
    scorepoints = {"alien_hit": 100, "ship_hit": -500, "ship_alien_collision": -1500}

    SCOREBOARD_FONT = "PressStart2P-vaV7.ttf"
    SCOREBOARD_FONT_PATH = os.path.join(FONTS_DIR, SCOREBOARD_FONT)

    SCORE_BOTTOMLEFT = (D_PADDING, D_HEIGHT - D_PADDING)
    LIVES_BOTTOMRIGHT = (D_WIDTH - D_PADDING, D_HEIGHT - D_PADDING)
    BOSS_LIVES_MIDBOTTOM = (D_WIDTH // 2, D_HEIGHT - D_PADDING)
