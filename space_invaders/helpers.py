"""
Helper module
"""
import os
import pygame


def get_scaled_image(source, scale):
    """Loades and returns the scaled image"""
    image = pygame.image.load(source).convert_alpha()
    scaled_size = (image.get_width() * scale, image.get_height() * scale)
    scaled_image = pygame.transform.scale(image, scaled_size)
    return scaled_image