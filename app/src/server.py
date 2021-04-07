import os
import flask
from flask import Flask
server = Flask(__name__)

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
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_battles(self):
        self.cursor.execute('SELECT * FROM Battle')
        rec = []
        for c in self.cursor:
            rec.append(c[2])
        return rec

@server.route("/")
def hello():
    conn = DBManager()
    rec = conn.query_battles()

    result = []
    for c in rec:
        result.append(c)

    return flask.jsonify({"response": result})

if __name__ == "__main__":
    # remove debug=True when deployed
    server.run(debug=True, host='0.0.0.0')

