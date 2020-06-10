import sqlite3
import os

from dotenv import load_dotenv
load_dotenv()

class DBManager:
    def __init__(self):
        try:
            connection = sqlite3.connect(os.getenv('DATABASE_NAME'))
            print('Connected to database')
            self.con = connection
        except:
            print('Error connecting to the database')
        
        self.builder = connection.cursor()

    def CreateTable(self):
        self.builder.execute("CREATE TABLE IF NOT EXISTS automessages(trigger text PRIMARY KEY, response text)")
        self.con.commit()

    def NewAutoMessage(self, trigger, response):
        if not self.GetAutoMessageResponse(trigger):
            self.builder.execute("INSERT INTO automessages VALUES('"+trigger+"','"+response+"')")
            self.con.commit()  
            return True
        else:
            return False

    def DeleteAutoMessage(self, trigger):
        if self.GetAutoMessageResponse(trigger):
            self.builder.execute('DELETE FROM automessages WHERE trigger="'+trigger+'"')
            self.con.commit()  
            return True
        else:
            return False

    def GetAutoMessageResponse(self, trigger):
        self.builder.execute('SELECT trigger, response FROM automessages WHERE trigger="'+trigger+'"')
        rows = self.builder.fetchall()
        if len(rows) == 0:
            return False
        else:
            return rows[0][1]

    def ResetDatabase(self):
        self.builder.execute('DROP TABLE IF EXISTS automessages')
        self.con.commit()
        self.CreateTable()
        return