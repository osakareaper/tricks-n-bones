import pygame
from controller.settings import *
from view.sprites import *

class Draw:
  def __init__(self, display_surface, player_instance, maps_instance):
    self.display_surface = display_surface
    self.player_instance = player_instance
    self.maps_instance = maps_instance
    

  def drawGUI(self):
    self.PLAYER = self.player_instance
    # game GUI
    self.display_surface.blit(FONT.render(str(self.PLAYER.nick)+"'s Adventure", 1, (255,255,255)), (20,0))
    self.display_surface.blit(FONT.render("LEVEL " + str(self.maps_instance.level_i + 1), 1, (255,255,255)), (660,0))
    self.display_surface.blit(heart, (20, 630))
    self.display_surface.blit(FONT.render("LIFES: " + str(self.PLAYER.lifes), 1, (255,255,255)), (50,620))
    self.display_surface.blit(bone, (140,630))
    self.display_surface.blit(FONT.render("BONES: " + str(self.PLAYER.bones), 1, (255,255,255)), (170,620))
    self.display_surface.blit(FONT.render("SCORE: " + str(self.PLAYER.score), 1, (255,255,255)), (600,620))
    self.display_surface.blit(candy, (570,630))