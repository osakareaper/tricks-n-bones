import pygame
import tkinter as tk
from tkinter import simpledialog
from view.sprites import *

class Player:
    def __init__(self, maps_instance):
        self.maps_instance = maps_instance

        self.nick = self.update_nickname()
        self.score = 0
        self.score_aux = 0
        self.lifes = 3
        self.bones = 0

        self.player = player_left
        self.posX = self.maps_instance.X_BEGIN
        self.posY = self.maps_instance.Y_BEGIN

    def get_nickname(self):
        try:
            with open('assets/nickname/nickname.txt', 'r') as file:
                nickname = file.read().strip()
                return nickname if nickname else "Tricky"
        except FileNotFoundError:
            return "Tricky"

    def set_nickname(self, nickname):
        try:
            with open('assets/nickname/nickname.txt', 'w') as file:
                file.write(nickname)
            return nickname
        except:
            return "Tricky"

    def update_nickname(self):
        root = tk.Tk()
        root.withdraw()

        nickname = simpledialog.askstring("Nickname", "Choose your Nickname:")
        return self.set_nickname(nickname) if nickname else "Tricky"

