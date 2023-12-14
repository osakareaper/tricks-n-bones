import pygame, sys, sqlite3
from model.sqlite import *
from model.player import Player
from view.menu import StartMenu
from view.gameOver import GameOver
from view.sounds import *
from view.draw import *
from view.win import *
from controller.settings import *
from controller.controller import *
from controller.levelConstructor import *
from controller.mapReader import *
from controller.nickGenerator import*

class Level():
 
  def __init__(self):
    # get the display surface
    self.menu = 1
    self.display_surface = pygame.display.get_surface()
    self.maps_instance = Maps()
    self.STARTMENU = StartMenu(self.menu)
    self.NICKGENERATOR = NickGenerator()
    self.PLAYER = Player(self.maps_instance, self.NICKGENERATOR)
    self.CONTROLLER = Controller(self.PLAYER, self.maps_instance)
    self.gameover_instance = GameOver(self.PLAYER)
    self.win_instance = Win(self.PLAYER)
    self.LEVELCONSTRUCTOR = levelConstructor(self.PLAYER, self.maps_instance, self.gameover_instance, self.win_instance)
    self.DRAW = Draw(self.display_surface, self.PLAYER, self.maps_instance)
    
  def run(self):
    db_init()
    
    # start menu
    self.STARTMENU.draw()

    # game screen
    self.display_surface.fill('black')
    self.DRAW.drawGUI()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
        # Controle do Player
        self.CONTROLLER.playerControl(event)

        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()

    self.LEVELCONSTRUCTOR.constructLevel()

  

      
    

