import pygame

class Level:
  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()

  def run(self, dt):
    self.display_surface.fill('gray')
