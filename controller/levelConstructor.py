import pygame
from model.sqlite import *
from controller.settings import *
from view.sprites import *
from view.sounds import *

class levelConstructor:
  def __init__(self, player_instance, maps_instance, gameover_instance, win_instance):
    self.display_surface = pygame.display.get_surface()
    self.player_instance = player_instance
    self.maps_instance = maps_instance
    self.gameover_instance = gameover_instance
    self.win_instance = win_instance
     
  def constructLevel(self):
      self.PLAYER = self.player_instance
      self.GAMEOVER = self.gameover_instance
      for y in range(0,30):
        for x in range(0,38):
          if self.maps_instance.m[y][x]=="0":
            self.display_surface.blit(empty_square,(x*SQUARE_SIZE,y*SQUARE_SIZE))
          elif self.maps_instance.m[y][x]=="1":
            self.display_surface.blit(lava,(x*SQUARE_SIZE,y*SQUARE_SIZE))
          elif self.maps_instance.m[y][x]=="2":
            self.display_surface.blit(floor,(x*SQUARE_SIZE,y*SQUARE_SIZE))
          elif self.maps_instance.m[y][x]=="3":
            self.display_surface.blit(floor,(x*SQUARE_SIZE,y*SQUARE_SIZE))
            self.display_surface.blit(chest,(x*SQUARE_SIZE,y*SQUARE_SIZE))
          elif self.maps_instance.m[y][x]=="4":
            self.display_surface.blit(wall,(x*SQUARE_SIZE,y*SQUARE_SIZE))
          elif self.maps_instance.m[y][x]=="5":
            self.display_surface.blit(stone,(x*SQUARE_SIZE,y*SQUARE_SIZE))


      if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] in ["1","3"]:
          
          if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)]=="1":
              death.play()
              self.PLAYER.lifes-=1
              self.PLAYER.score -= self.PLAYER.score_aux
              self.PLAYER.score_aux = 0
              self.PLAYER.hasKey = False
              self.PLAYER.key = 0

              if self.PLAYER.lifes==0:
                insert_player(self.PLAYER)
                self.GAMEOVER.draw()
      
              else:
                  
                  self.maps_instance.m = list(map(lambda x:list(x),open("assets/levels/"+self.maps_instance.level_names[self.maps_instance.level_i]+".txt","r").read().splitlines()))
                  self.PLAYER.posX= self.maps_instance.X_BEGIN
                  self.PLAYER.posY= self.maps_instance.Y_BEGIN
              
          else:

              self.PLAYER.bones += 1
              self.PLAYER.score_aux = 0
              self.maps_instance.level_i+=1

              if self.maps_instance.level_i == 16:
                self.win_instance.draw()

              else:
                nextLevel.play()
                self.maps_instance.m = list(map(lambda x:list(x),open("assets/levels/"+self.maps_instance.level_names[self.maps_instance.level_i]+".txt","r").read().splitlines()))
                
                self.maps_instance.VALUES_XY = open("assets/levels/"+self.maps_instance.level_names[self.maps_instance.level_i]+".txt","r").read().splitlines()[30].split(" ")
                self.maps_instance.X_BEGIN = int(self.maps_instance.VALUES_XY[0])*SQUARE_SIZE
                self.maps_instance.Y_BEGIN = int(self.maps_instance.VALUES_XY[1])*SQUARE_SIZE
                self.PLAYER.posX= self.maps_instance.X_BEGIN
                self.PLAYER.posY= self.maps_instance.Y_BEGIN
        
              
          
                  
      else:
          self.display_surface.blit(self.PLAYER.player,(self.PLAYER.posX,self.PLAYER.posY))
          pygame.display.update()
