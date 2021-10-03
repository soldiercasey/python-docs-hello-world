from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Back up before you get smacked up!!"
