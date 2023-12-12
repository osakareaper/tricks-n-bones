import pygame, sys
from settings import *
from my_libraries.player import *

class GameOver():
  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.menu = 1
    self.PLAYER = Player()

  def run(self):
    while self.menu == 1:
      self.display_surface.fill('black')
      self.display_surface.blit(TITLE_FONT.render("GAME OVER!", 1, (255,0,0)), (320,SCREEN_HEIGHT/2-150))
      self.display_surface.blit(FONT.render("press ESC to exit", 1, (255,255,255)), (305,SCREEN_HEIGHT/2-100))
      self.display_surface.blit(FONT.render("Your Score:", 1, (255,255,255)), (330,SCREEN_HEIGHT/2))
      self.display_surface.blit(FONT.render(str(self.PLAYER.score), 1, ('yellow')), (SCREEN_WIDTH/2,SCREEN_HEIGHT/2+35))
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()



