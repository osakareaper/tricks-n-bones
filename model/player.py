import pygame

class Player:
  def __init__(self, maps_instance, nick_generator_instance):
    self.maps_instance = maps_instance

    self.nick_generator_instance = nick_generator_instance

    self.nick = self.nick_generator_instance.getRandomNick()

    self.score = 0
    self.score_aux = 0
    self.lifes = 3
    self.bones = 0

    self.player = pygame.image.load("assets/graphics/player.png")
    self.posX = self.maps_instance.X_BEGIN
    self.posY = self.maps_instance.Y_BEGIN
