
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


@server.route("/battle/add", methods=['GET', 'POST'])
def battle_add():
    user = {'username': 'Themien'}
    form = forms.BattleForm()
    if form.validate_on_submit():
        # Add the battle here
        battle_controller.add_battle(form)
        return redirect('/test_query')
    return render_template('form.html', title='Add battle', user=user, form=form)  


@server.route("/test_query")
def query_db():
    # battle_controller.conn.add_battle()
    rec = battle_controller.conn.query_battles()
    result = []
    for c in rec:
        result.append(c)

    return flask.jsonify({"response": result})

if __name__ == "__main__":
    # remove debug=True when deployed
    server.run(debug=True, host='0.0.0.0')

