import sqlite3

def db_init():
    conn = sqlite3.connect('players.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS players (
                nick text,
                score integer
            )""")


def insert_player(player):
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO players VALUES (:nick, :score)", {'nick': player.nick, 'score': player.score})


def get_players():
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    return c.fetchall()


def update_score(player, score):
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    with conn:
        c.execute("""UPDATE players SET score = :score
                    WHERE nick = :nick""",
                  {'nick': player.nick, 'score': score})


def remove_player(player):
    conn = sqlite3.connect('players.db')
    c = conn.cursor()
    with conn:
        c.execute("DELETE from players WHERE nick = :nick",
                  {'nick': player.nick})

