import pygame, os

# Settings Document
pygame.font.init()

WINDOW_TITLE = "Tricks n' Bones"

SCREEN_DIMENSIONS = (SCREEN_WIDTH,SCREEN_HEIGHT) = (760, 680)
SQUARE_SIZE = 20

FPS = 60

# Importação da FOnte
FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixeled.ttf'), 12)

# COLORS

FLOOR_COLOR = (108,117,125)