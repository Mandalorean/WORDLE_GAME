import sqlite3


def everyGameDb(games_played, todays_word, attempt, completed, entered_words):
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute(
        '''CREATE TABLE if not exists Wordle (GameNum Integer, WordSelected text, Attempts Integer, Successful text, Attempted_Words text)''')

    c.execute("INSERT INTO Wordle VALUES (?,?,?,?,?)",
              (games_played, todays_word, attempt, completed, entered_words))

    con.commit()

    con.close()


def queryWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("SELECT * FROM wordle")
    for column in c.description:
        print(column[0], end=" ")
    print()
    print(c.fetchall())
    con.close()


def truncateWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DELETE FROM wordle")
    con.commit()
    con.close()


def dropWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DROP TABLE if exists wordle")
    con.commit()
    con.close()


def calcStats():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DROP TABLE if exists WordleStats")

    c.execute(
        '''CREATE TABLE if not exists WordleStats (SuccessfulGames Integer, UnsuccessfulGames Integer, AverageAttemptsToWin Integer)''')

    c.execute("DELETE FROM WordleStats")

    c.execute("SELECT AVG(Attempts) FROM wordle where Attempts != -1")

    avgAttemptsToWin = c.fetchall()[0][0]

    c.execute("SELECT COUNT(*) FROM wordle where Attempts = -1")

    unsuccessful = c.fetchall()[0][0]

    c.execute("SELECT COUNT(*) FROM wordle where Attempts != -1")

    successful = c.fetchall()[0][0]

    c.execute("INSERT INTO WordleStats VALUES (?,?,?)",
              (successful, unsuccessful, avgAttemptsToWin))

    c.execute("SELECT * FROM WordleStats")
    for column in c.description:
        print(column[0], end=" ")
    con.commit()
    print()
    print(c.fetchall()[0])

    con.close()


# dropWordle()
# queryWordle()
calcStats()
