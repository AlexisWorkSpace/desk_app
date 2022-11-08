import sqlite3

class Connection:
    def __init__(self):
        self.db = '../db/database.db'
        self.con = sqlite3.connect(self.db)
        self.cursor = self.con.cursor()

    def close_db(self):
        self.con.commit()
        self.con.close()
