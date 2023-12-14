import random

class NickGenerator():

  def getRandomNick(self):
    with open("assets/nicks/nicks_list.txt", "r", encoding="utf-8") as nicks:
        nicks = nicks.readlines()

    # Escolher um nome aleatório da lista
    random_nick = random.choice(nicks).strip()
    
    return random_nick