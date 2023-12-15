import pygame
from controller.settings import *

# Sprites

lava = pygame.image.load("assets/graphics/lava.png")
stone = pygame.image.load("assets/graphics/stone.png")
floor = pygame.image.load("assets/graphics/floor.png")
wall = pygame.image.load("assets/graphics/wall.png")
chest = pygame.image.load("assets/graphics/chest.png")
candy = pygame.image.load("assets/graphics/candy.png")
heart = pygame.image.load("assets/graphics/heart.png")
bone = pygame.image.load("assets/graphics/bone.png")
player_left = pygame.image.load("assets/graphics/player_left.png")
player_right = pygame.image.load("assets/graphics/player_right.png")

empty_square = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
empty_square.fill((20,20,20))