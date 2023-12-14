from controller.settings import *

# Leitura dos Mapas
class Maps():
  def __init__(self):
    self.level_names = ["level1","level2","level3","level4","level5","level6","level7","level8","level9","level10","level11","level12","level13","level14","level15","level16"]
    self.level_i = 0
    self.m = list(map(lambda x:list(x),open("assets/levels/"+self.level_names[self.level_i]+".txt","r").read().splitlines()))

    self.VALUES_XY = open("assets/levels/"+self.level_names[self.level_i]+".txt","r").read().splitlines()[30].split(" ")
    self.X_BEGIN = int(self.VALUES_XY[0])*SQUARE_SIZE
    self.Y_BEGIN = int(self.VALUES_XY[1])*SQUARE_SIZE