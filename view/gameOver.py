import pygame, sys
from controller.settings import *

class GameOver():
  def __init__(self, player_instance):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.menu = 1
    self.player_instance = player_instance

  def draw(self):
    while self.menu == 1:
      
      gameover = BIGGER_FONT.render("GAME OVER!", 1, (255,0,0))
      gameover_rect = gameover.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-250))


      playername = TITLE_FONT.render(str(self.player_instance.nick), 1, (255,0,0))
      playername_rect = playername.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-100))

      yourscore = FONT.render("Your SCORE was:", 1, (255,255,255))
      yourscore_rect = yourscore.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-50))

      score = FONT.render(str(self.player_instance.score), 1, ('yellow'))
      score_rect = score.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-25))

      esc = FONT.render("press ESC to exit", 1, (255,255,255))
      esc_rect = esc.get_rect(center=(SCREEN_WIDTH//2, 600))

      self.display_surface.fill('black')
      self.display_surface.blit(gameover, gameover_rect)
      self.display_surface.blit(playername, playername_rect)
      self.display_surface.blit(yourscore, yourscore_rect)
      self.display_surface.blit(score, score_rect)
      self.display_surface.blit(esc, esc_rect)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            



