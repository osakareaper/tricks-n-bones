import pygame, os

# Settings Document

# Font Settings
pygame.font.init()
FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixeled.ttf'), 12)
TITLE_FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixeled.ttf'), 16)
BIGGER_FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixeled.ttf'), 20)

# Screen Settings
WINDOW_TITLE = "Tricks n' Bones"

SCREEN_DIMENSIONS = (SCREEN_WIDTH,SCREEN_HEIGHT) = (760, 680)
SQUARE_SIZE = 20

FPS = 60


LAVA = "1"
CHAO = "2"
BAU = "3"
PAREDE = "4"
PEDRA = "5"
CHAVE = "6"

