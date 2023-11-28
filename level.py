import pygame
from settings import *
from my_libraries.player import *

#  Levels
level_names = ["level1","level2","level3","level4","level5","level6","level7","level8","level9","level10","level11","level12","level13","level14","level15","level16"]
level_i = 0
m = list(map(lambda x:list(x),open("assets/levels/"+level_names[level_i]+".txt","r").read().splitlines()))

# Sprites
# player = pygame.image.load("assets/graphics/Player.png")

# water = pygame.image.load("assets/graphics/Water.png")




# double_ice = pygame.image.load("assets/graphics/DoubleIce.png")

# score_screen = pygame.image.load("assets/graphics/score_screen.png")

floor = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
floor.fill(FLOOR_COLOR)

wall = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
wall.fill((2,48,32))

empty_square = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
empty_square.fill((48,52,52))

finish_square = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
finish_square.fill((255,195,0))







class Level:
  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    self.PLAYER = Player()

  def run(self, dt):
    self.display_surface.fill('black')
    self.display_surface.blit(FONT.render("LIFES: " + str(self.PLAYER.lifes), 1, (255,255,255)), (20,620))
    self.display_surface.blit(FONT.render("BONES: " + str(self.PLAYER.bones), 1, (255,255,255)), (110,620))
    self.display_surface.blit(FONT.render("SCORE: " + str(self.PLAYER.score), 1, (255,255,255)), (600,620))

    for y in range(0,30):
      for x in range(0,38):
        if m[y][x]=="0":
          self.display_surface.blit(empty_square,(x*SQUARE_SIZE,y*SQUARE_SIZE))
        #elif m[y][x]=="1":
          #self.display_surface.blit(water,(x*SQUARE_SIZE,y*SQUARE_SIZE))
        elif m[y][x]=="2":
          self.display_surface.blit(floor,(x*SQUARE_SIZE,y*SQUARE_SIZE))
        elif m[y][x]=="3":
          self.display_surface.blit(finish_square,(x*SQUARE_SIZE,y*SQUARE_SIZE))
        elif m[y][x]=="4":
          self.display_surface.blit(wall,(x*SQUARE_SIZE,y*SQUARE_SIZE))
        #elif m[y][x]=="5":
          #self.display_surface.blit(double_ice,(x*SQUARE_SIZE,y*SQUARE_SIZE))
