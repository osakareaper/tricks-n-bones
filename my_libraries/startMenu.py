import pygame, sys
from settings import *

class StartMenu():
  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.menu = 1

  def run(self):
    while self.menu == 1:
      self.display_surface.fill('black')
      self.display_surface.blit(TITLE_FONT.render("TRICKS N' BONES", 1, (255,255,255)), (285,120))
      self.display_surface.blit(FONT.render("press SPACE to play", 1, (255,0,0)), (290,SCREEN_HEIGHT/2))
      self.display_surface.blit(FONT.render("press ESC to exit", 1, (255,0,0)), (300,SCREEN_HEIGHT/2+50))
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.menu = 2
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()



