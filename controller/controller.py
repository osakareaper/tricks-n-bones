import pygame, random
from controller.settings import *
from view.sounds import *
from view.sprites import *

class Controller():
  def __init__(self, player_instance, maps_instance):
    self.player_instance = player_instance
    self.maps_instance = maps_instance

  def playerControl(self, event):
      
      self.PLAYER = self.player_instance

      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
              # Se nao for PAREDE, se move
              if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] != PAREDE:
                self.PLAYER.posX -= SQUARE_SIZE
                self.player_instance.player = player_left
                walk.play()
                
                # Se for PEDRA
                if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] == PEDRA:
                  scoreUp.play()
                  self.PLAYER.score += 100
                  self.PLAYER.score_aux += 100
                  self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] = CHAO

              # Se for CHÃO
                elif self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] == CHAO:
                  self.PLAYER.score += 10
                  self.PLAYER.score_aux += 10
                  self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] = LAVA

            if event.key == pygame.K_RIGHT:
              # Se nao for PAREDE, se move
              if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] != PAREDE:
                self.PLAYER.posX += SQUARE_SIZE
                self.player_instance.player = player_right
                walk.play()
                
                # Se for PEDRA
                if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] == PEDRA:
                  scoreUp.play()
                  self.PLAYER.score += 100
                  self.PLAYER.score_aux += 100
                  self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] = CHAO
              
                # Se for CHÃO
                elif self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] == CHAO:
                  self.PLAYER.score += 10
                  self.PLAYER.score_aux += 10
                  self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] = LAVA

            if event.key == pygame.K_DOWN:
              # Se nao for PAREDE, se move
              if self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] != PAREDE:
                self.PLAYER.posY += SQUARE_SIZE
                walk.play()
                
                # Se for PEDRA
                if self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == PEDRA:
                  scoreUp.play()
                  self.PLAYER.score += 100
                  self.PLAYER.score_aux += 100
                  self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = CHAO

                # Se for CHÃO
                elif self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == CHAO:
                  self.PLAYER.score += 10
                  self.PLAYER.score_aux += 10
                  self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = LAVA

            if event.key == pygame.K_UP:
              # Se nao for PAREDE, se move
              if self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] != PAREDE:
                self.PLAYER.posY -= SQUARE_SIZE
                walk.play()
                
                # Se for PEDRA
                if self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == PEDRA:
                  scoreUp.play()
                  self.PLAYER.score += 100
                  self.PLAYER.score_aux += 100
                  self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = CHAO

                # Se for CHÃO
                elif self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == CHAO:
                  self.PLAYER.score += 10
                  self.PLAYER.score_aux += 10
                  self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = LAVA      