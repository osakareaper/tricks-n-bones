import pygame
from settings import Maps

class Player:
  def __init__(self):
    self.score = 0
    self.score_aux = 0
    self.lifes = 3
    self.bones = 0

    self.player = pygame.image.load("assets/graphics/player.png")
    maps_instance = Maps()
    self.posX = maps_instance.X_BEGIN
    self.posY = maps_instance.Y_BEGIN