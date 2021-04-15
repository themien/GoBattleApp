
from datetime import date, datetime, time, timedelta
import models

class BattleController:

    # should this be here?
    def __init__(self):
        self.conn = models.DBManager()

    
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
        tomorrow = datetime.now().date() + timedelta(days=1)   
        

        self.conn.add_battle(battle)

        

