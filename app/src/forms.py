from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField, TimeField, IntegerField
from wtforms.validators import DataRequired

class BattleForm(FlaskForm):
    season = IntegerField('Season')
    league = StringField('League')
    elo = IntegerField('Elo')
    battle_date = DateField('Date')
    battle_time = TimeField('Time')
    my_pokemon_1 = StringField('My First Pokemon')
    my_pokemon_2 = StringField('My Second Pokemon')
    my_pokemon_3 = StringField('My Third Pokemon')
    opponent_name = StringField('Opponent', validators=[DataRequired()])
    opponent_pokemon_1 = StringField('Opponent First Pokemon', validators=[DataRequired()])
    opponent_pokemon_2 = StringField('Opponent Second Pokemon', validators=[DataRequired()])
    opponent_pokemon_3 = StringField('Opponent Third Pokemon', validators=[DataRequired()])
    is_won = BooleanField('Battle won?')
    if_lost_was_badly_played = BooleanField('If lost was it badly played?')   
    submit = SubmitField('Add')