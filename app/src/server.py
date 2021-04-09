import flask
from flask import Flask, render_template
server = Flask(__name__)

import models
import forms

@server.route("/")
@server.route("/index")
@server.route("/home")
def index():
    user = {'username': 'Themien'}
    return render_template('base.html', title='Home', user=user)  


# @server.route("/form")
# def form():
#     user = {'username': 'Themien'}
#     form = form.TestForm()
#     return render_template('form.html', title='Home', user=user, form=form)  


@server.route("/test_query")
def query_db():
    conn = models.DBManager()
    conn.add_battle()
    rec = conn.query_battles()
    result = []
    for c in rec:
        result.append(c)

    return flask.jsonify({"response": result})

if __name__ == "__main__":
    # remove debug=True when deployed
    server.run(debug=True, host='0.0.0.0')

