
import mysql.connector
from datetime import date, datetime, time, timedelta

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
    

    def add_battle(self):
        tomorrow = datetime.now().date() + timedelta(days=1)
        add_battle = ("INSERT INTO Battle"
                      "(battleId, season, league, battleDate, battleTime,"
                      "myPokemon1, myPokemon2, myPokemon3, opponentName,"
                      "opponentPokemon1, opponentPokemon2, opponentPokemon3,"
                      "isWon, ifLostWasBadPlayed)"
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        
        data_battle = (2, 7, 'Great', date(1977, 6, 14), time(14,32,5), 'Talo', 'Mew', 'Machamp', 'oppo2', 'Celebi', 'Mantine', 'Pelipper', False, True)
        
        # Insert new employee
        self.cursor.execute(add_battle, data_battle)
        # emp_no = cursor.lastrowid
        
        # # Insert salary information
        # data_salary = {
        #   'emp_no': emp_no,
        #   'salary': 50000,
        #   'from_date': tomorrow,
        #   'to_date': date(9999, 1, 1),
        # }
        # self.cursor.execute(add_salary, data_salary)
            
    def query_battles(self):
        self.cursor.execute('SELECT * FROM Battle')
        rec = []
        for c in self.cursor:
            rec.append(c[2])
        return rec


class Battle:
    def __init__(self, battleId, season, league, battleDate, battleTime, 
                 myPokemon1, myPokemon2, myPokemon3, opponentName, 
                 opponentPokemon1, opponentPokemon2, opponentPokemon3,
                 isWon, ifLostWasBadPlayed):
        self.battleId = battleId
        self.season = season
        self.league = league
        self.battleDate = battleDate
        self.battleTime = battleTime
        self.myPokemon1 = myPokemon1
        self.myPokemon2 = myPokemon2
        self.myPokemon3 = myPokemon3
        self.opponentName = opponentName
        self.opponentPokemon1 = opponentPokemon1
        self.opponentPokemon2 = opponentPokemon2
        self.opponentPokemon3 = opponentPokemon3
        self.isWon = isWon
        self.ifLostWasBadPlayed = ifLostWasBadPlayed