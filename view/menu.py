import pygame, sys
from model.sqlite import *
from controller.settings import *

class StartMenu():
  def __init__(self, menu_instance):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.menu_instance = menu_instance

  def draw(self):
    while self.menu_instance == 1:
      self.display_surface.fill('black')
      self.display_surface.blit(TITLE_FONT.render("TRICKS N' BONES", 1, (255,255,255)), (285,120))
      self.display_surface.blit(FONT.render("press SPACE to play", 1, (255,0,0)), (290,SCREEN_HEIGHT/2))
      self.display_surface.blit(FONT.render("press BKSPC to scoreboard", 1, (255,0,0)), (270,SCREEN_HEIGHT/2+50))
      self.display_surface.blit(FONT.render("press ESC to exit", 1, (255,0,0)), (300,SCREEN_HEIGHT/2+100))
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

        elif event.type == pygame.KEYDOWN:
          
          if event.key == pygame.K_SPACE:
            self.menu_instance = 3

          if event.key == pygame.K_BACKSPACE:
            self.menu_instance = 2
            players = get_players()
            players.sort(reverse=True, key=lambda player:player[1])

            while self.menu_instance == 2:
              self.display_surface.fill('black')
              self.display_surface.blit(TITLE_FONT.render("SCOREBOARD", 1, (0,255,0)), (320,50))
              y_pos = 100

              for player in players[:5]:
                  self.display_surface.blit(FONT.render(player[0], 1, (255, 255, 255)), (320, y_pos))
                  self.display_surface.blit(FONT.render(str(player[1]), 1, (255, 255, 255)), (600, y_pos))
                  y_pos+=50

              self.display_surface.blit(FONT.render("press BKSPC to go back", 1, (255,255,255)), (305,540))
      
              pygame.display.update()

              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()

                elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                  if event.key == pygame.K_BACKSPACE:
                    self.menu_instance = 1

          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
      



