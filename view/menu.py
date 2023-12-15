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

      # texts and rects
      title = TITLE_FONT.render("Tricks n' Bones", 1, (255,255,255))
      title_rect = title.get_rect(center=(SCREEN_WIDTH//2,100))

      play = FONT.render("press SPACE to play", 1, (0,255,0))
      play_rect = play.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

      scoreboard = FONT.render("press BKSPC to scoreboard", 1, (0,0,255))
      scoreboard_rect = scoreboard.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+50))

      esc = FONT.render("press ESC to exit", 1, (255,0,0))
      esc_rect = esc.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100))

      options = FONT.render("press Q to options", 1, (255,255,255))
      options_rect = options.get_rect(center=(650,650))

      self.display_surface.fill('black')
      self.display_surface.blit(title, title_rect)
      self.display_surface.blit(play, play_rect)
      self.display_surface.blit(scoreboard, scoreboard_rect)
      self.display_surface.blit(esc, esc_rect)
      self.display_surface.blit(options, options_rect)
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

              # texts and rects
              scoreboardTitle = TITLE_FONT.render("SCOREBOARD", 1, (0,255,0))
              scoreboardTitle_rect = scoreboardTitle.get_rect(center=(SCREEN_WIDTH//2,30))

              self.display_surface.fill('black')
              self.display_surface.blit(scoreboardTitle, scoreboardTitle_rect)

              # print top scores
              y_pos = 100
              index = 1

              for player in players[:10]:
                position = FONT.render(str(index), 1, (0, 0, 255))
                position_rect = position.get_rect(center=(20, y_pos))

                playerName = FONT.render(player[0], 1, (255, 255, 255))
                playerName_rect = playerName.get_rect()
                playerName_rect.midleft = (40, y_pos)

                playerScore = FONT.render(str(player[1]), 1, (255, 255, 255))
                playerScore_rect = playerScore.get_rect(center=(SCREEN_WIDTH-50, y_pos))

                self.display_surface.blit(position, position_rect)
                self.display_surface.blit(playerName, playerName_rect)
                self.display_surface.blit(playerScore, playerScore_rect)
                y_pos+=50
                index+=1

              goBack = FONT.render("press BKSPC to go back", 1, (255,255,255))
              goBack_rect = goBack.get_rect(center=(SCREEN_WIDTH//2, 640))

              self.display_surface.blit(goBack, goBack_rect)
      
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
      



