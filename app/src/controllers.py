import models

class BattleController:

    def __init__(self):
        self.conn = models.DBManager()

    # Handeles communication between db and server
    def add_battle(self, form):
        battle = models.Battle(3,
                               form.season.data,
                               form.league.data,
                               form.elo.data,
                               form.battle_date.data,
                               form.battle_time.data,
                               form.my_pokemon_1.data,
                               form.my_pokemon_2.data,
                               form.my_pokemon_3.data,
                               form.opponent_name.data,
                               form.opponent_pokemon_1.data,
                               form.opponent_pokemon_2.data,
                               form.opponent_pokemon_3.data,
                               form.is_won.data,
                               form.if_lost_was_badly_played.data,
                               )

        #
        #Here validate inputs and add defaults for uncomplete form fields
        #

        add_query = ("INSERT INTO Battle"
                      "(battleId, season, league, elo, battleDate, battleTime,"
                      "myPokemon1, myPokemon2, myPokemon3, opponentName,"
                      "opponentPokemon1, opponentPokemon2, opponentPokemon3,"
                      "isWon, ifLostWasBadPlayed)"
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        
        data_battle = (battle.battleId, 
                       battle.season,
                       battle.league,
                       battle.elo,
                       battle.battleDate,
                       battle.battleTime,
                       battle.myPokemon1,
                       battle.myPokemon2,
                       battle.myPokemon3,
                       battle.opponentName,
                       battle.opponentPokemon1,
                       battle.opponentPokemon2,
                       battle.opponentPokemon3,
                       battle.isWon,
                       battle.ifLostWasBadPlayed)

        self.conn.cursor.execute(add_query, data_battle)

        

