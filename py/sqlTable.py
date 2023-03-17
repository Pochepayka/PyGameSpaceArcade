import sqlite3
import logging


class Endpoint:
    connection = None
    cursor = None

    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
        try:
            self.connection = sqlite3.connect("sqlTable.db")
            self.cursor = self.connection.cursor()
            logging.info("Endpoint activated.")
        except Exception as ex:
            logging.error("Connection disabled.")

    def tryCreateTable(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS players
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
               nickname TEXT UNIQUE, 
                score INTEGER)
            """)
            logging.info("Table ready.")
        except Exception as ex:
            logging.error("Can't create table.")

    def selectTopFive(self):
        try:
            result = self.cursor.execute("""SELECT  nickname,score
                                    FROM players 
                                    ORDER BY score desc
                                    LIMIT 5
                                    """).fetchall()
            logging.info("Select from players.")
            return result
        except Exception as ex:
            logging.error("Selection error")

    def saveResult(self, player):
        try:
            self.cursor.execute(
                'REPLACE INTO  players(nickname,score)  VALUES(' + "'" + player["nickname"].__str__() + "'" + "," +
                player["score"].__str__() + ")")
            self.connection.commit()
            logging.info("Insert player data")
        except Exception as ex:
            logging.error("Cant execute save data")