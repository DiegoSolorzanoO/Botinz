import sqlite3
import os

from dotenv import load_dotenv
load_dotenv()

class DBManager:
    def __init__(self):
        try:
            connection = sqlite3.connect(os.getenv('DATABASE_NAME'))
            print('Connected')
        except:
            print('Error connecting to the database')
        
        self.builder = connection.cursor()

    def CreateTable(self):
        self.builder.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")