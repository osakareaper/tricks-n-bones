import pygame
import sqlite3
from settings import Maps

class Player:
    def __init__(self):
        self.score = 0
        self.score_aux = 0
        self.lifes = 3
        self.bones = 0

        self.player = pygame.image.load("assets/graphics/player.png")
        maps_instance = Maps()
        self.posX = maps_instance.X_BEGIN
        self.posY = maps_instance.Y_BEGIN

    def init(self):
        conn = sqlite3.connect('players.db')

        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS players (
                nickname TEXT,
                score INTEGER
            ) 
        """)

        conn.commit()
        conn.close()

    def insert_player(player):
        with conn:
            c.execute("INSERT INTO players VALUES (?, ?)", 
                      (player.nickname, player.score))

    def get_players():
        c.execute("SELECT * FROM players")
        return c.fetchall()

    def update_score(player, score):
        with conn:
            c.execute("""
                      UPDATE players SET score = :score
                      WHERE nickname = :nick
␓                      """, {'score': score, 'nick': player.nickname})

    def remove_player(nick):
        with conn:
            c.execute("DELETE FROM players WHERE nickname= :nick", ('nick': nick))

