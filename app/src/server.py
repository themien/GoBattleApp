
import flask
from flask import Flask, render_template, flash, redirect
from config import Config

server = Flask(__name__)
server.config.from_object(Config)

# local modules
import models
import forms
import controllers

battle_controller = controllers.BattleController()

@server.route("/")
@server.route("/index")
@server.route("/home")
def index():
    user = {'username': 'Themien'}
    return render_template('base.html', title='Home', user=user)  


@server.route("/battles/add", methods=['GET', 'POST'])
def battle_add():
    user = {'username': 'Themien'}
    form = forms.BattleForm()
    if form.validate_on_submit():
        # Add the battle here
        battle_controller.add_battle_to_db(form)
        return redirect('/test_query')
    return render_template('battle_form.html', title='Add battle', user=user, form=form)  


@server.route("/battles/view")
def query_db():
    user = {'username': 'Themien'}
    data = battle_controller.query_battles_from_db()
    return render_template('battles_table.html', user=user, data=data)


if __name__ == "__main__":
    # remove debug=True when deployed
    server.run(debug=True, host='0.0.0.0')

