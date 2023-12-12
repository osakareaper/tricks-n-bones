import sys, pygame, os
from settings import *
from level import Level

class Game:
  def __init__(self):
    pygame.init() 
    self.SCREEN = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    self.CLOCK = pygame.time.Clock()
    self.LEVEL = Level()

  # MAIN LOOP
  def run(self):
    while True:
      # Delta Time
      dt = self.CLOCK.tick(FPS) / 1000
      # Run
      self.LEVEL.run(dt)

      pygame.display.update()
  
if __name__ == '__main__':
  game = Game()
  game.run()