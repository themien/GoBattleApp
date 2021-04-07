
import mysql.connector

class DBManager:
    def __init__(self, database='PoGoBattles', host="db", user="root", password="password"):
        self.connection = mysql.connector.connect(
            user=user, 
            password=password,
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_battles(self):
        self.cursor.execute('SELECT * FROM Battle')
        rec = []
        for c in self.cursor:
            rec.append(c[2])
        return rec


class Battle:
    def __init__(self):
        pass