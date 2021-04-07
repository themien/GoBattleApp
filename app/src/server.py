from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Damiano"

if __name__ == "__main__":
    # remove debug=True when deployed
   server.run(debug=True, host='0.0.0.0')