import pygame, sys
from settings import *
from settings import Maps
from my_libraries.player import Player
from my_libraries.startMenu import StartMenu
from my_libraries.gameOver import GameOver

# Sounds

pygame.mixer.init()

scoreUp = pygame.mixer.Sound("assets/sounds/scoreUp.wav")
nextLevel = pygame.mixer.Sound("assets/sounds/nextLevel.wav")

# Sprites

lava = pygame.image.load("assets/graphics/lava.png")
stone = pygame.image.load("assets/graphics/stone.png")
floor = pygame.image.load("assets/graphics/floor.png")
wall = pygame.image.load("assets/graphics/wall.png")
chest = pygame.image.load("assets/graphics/chest.png")

empty_square = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
empty_square.fill((20,20,20))

# Level

class Level():

  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.PLAYER = Player()
    self.STARTMENU = StartMenu()
    self.GAMEOVER = GameOver()
    self.maps_instance = Maps()

  def run(self, dt):
    # start menu
    self.STARTMENU.run()

    # game
    self.display_surface.fill('black')
    self.display_surface.blit(FONT.render("LIFES: " + str(self.PLAYER.lifes), 1, (255,255,255)), (20,620))
    self.display_surface.blit(FONT.render("BONES: " + str(self.PLAYER.bones), 1, (255,255,255)), (110,620))
    self.display_surface.blit(FONT.render("SCORE: " + str(self.PLAYER.score), 1, (255,255,255)), (600,620))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          # Se nao for PAREDE, se move
          if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] != PAREDE:
            self.PLAYER.posX -= SQUARE_SIZE
            
            # Se for PEDRA
            if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] == PEDRA:
              scoreUp.play()
              self.PLAYER.score += 100
              self.PLAYER.score_aux += 100
              self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] = CHAO

            # Se for CHÃO
            elif self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] == CHAO:
              self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] = LAVA

        if event.key == pygame.K_RIGHT:
          # Se nao for PAREDE, se move
          if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX+SQUARE_SIZE)/SQUARE_SIZE)] != PAREDE:
            self.PLAYER.posX += SQUARE_SIZE
            
            # Se for PEDRA
            if self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] == PEDRA:
              scoreUp.play()
              self.PLAYER.score += 100
              self.PLAYER.score_aux += 100
              self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] = CHAO

            # Se for CHÃO
            elif self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] == CHAO:
              self.maps_instance.m[int(self.PLAYER.posY/SQUARE_SIZE)][int((self.PLAYER.posX-SQUARE_SIZE)/SQUARE_SIZE)] = LAVA

        if event.key == pygame.K_DOWN:
          # Se nao for PAREDE, se move
          if self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] != PAREDE:
            self.PLAYER.posY += SQUARE_SIZE
            
            # Se for PEDRA
            if self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == PEDRA:
              scoreUp.play()
              self.PLAYER.score += 100
              self.PLAYER.score_aux += 100
              self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = CHAO

            # Se for CHÃO
            elif self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == CHAO:
              self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = LAVA

        if event.key == pygame.K_UP:
          # Se nao for PAREDE, se move
          if self.maps_instance.m[int((self.PLAYER.posY-SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] != PAREDE:
            self.PLAYER.posY -= SQUARE_SIZE
            
            # Se for PEDRA
            if self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == PEDRA:
              scoreUp.play()
              self.PLAYER.score += 100
              self.PLAYER.score_aux += 100
              self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = CHAO

            # Se for CHÃO
            elif self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] == CHAO:
              self.maps_instance.m[int((self.PLAYER.posY+SQUARE_SIZE)/SQUARE_SIZE)][int(self.PLAYER.posX/SQUARE_SIZE)] = LAVA      

    # LEVEL CONSTRUCTOR
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

            self.PLAYER.lifes-=1
            self.PLAYER.score -= self.PLAYER.score_aux
            self.PLAYER.score_aux = 0

            if self.PLAYER.lifes==0:

              self.GAMEOVER.run()
    
            else:
                
                self.maps_instance.m = list(map(lambda x:list(x),open("assets/levels/"+self.maps_instance.level_names[self.maps_instance.level_i]+".txt","r").read().splitlines()))
                self.PLAYER.posX= self.maps_instance.X_BEGIN
                self.PLAYER.posY= self.maps_instance.Y_BEGIN
            
        else:

            self.PLAYER.bones += 1
            self.PLAYER.score_aux = 0
            self.maps_instance.level_i+=1
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

