import flask
from flask import Flask
server = Flask(__name__)

import models

@server.route("/")
def hello():
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

