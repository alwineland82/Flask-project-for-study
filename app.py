from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife.counter = 0
    GameOfLife(25, 15)
    return render_template("index.html")


@app.route('/live')
def live():
    game = GameOfLife(25, 15)
    game.form_new_generation()
    return render_template("live.html", game=game, len=len)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
