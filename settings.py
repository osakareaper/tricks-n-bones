import pygame, os



# Settings Document
pygame.font.init()

WINDOW_TITLE = "Tricks n' Bones"

SCREEN_DIMENSIONS = (SCREEN_WIDTH,SCREEN_HEIGHT) = (760, 680)
SQUARE_SIZE = 20

FPS = 60

LAVA = "1"
CHAO = "2"
BAU = "3"
PAREDE = "4"
PEDRA = "5"

# Importação da FOnte
FONT = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixeled.ttf'), 12)

# COLORS

FLOOR_COLOR = (108,117,125)

class Maps():
  def __init__(self):
    self.level_names = ["level1","level2","level3","level4","level5","level6","level7","level8","level9","level10","level11","level12","level13","level14","level15","level16"]
    self.level_i = 0
    self.m = list(map(lambda x:list(x),open("assets/levels/"+self.level_names[self.level_i]+".txt","r").read().splitlines()))

    self.VALUES_XY = open("assets/levels/"+self.level_names[self.level_i]+".txt","r").read().splitlines()[30].split(" ")
    self.X_BEGIN = int(self.VALUES_XY[0])*SQUARE_SIZE
    self.Y_BEGIN = int(self.VALUES_XY[1])*SQUARE_SIZE