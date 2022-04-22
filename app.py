from flask import Flask, render_template


app = Flask(__name__)

@app.route('/<x>/')
def index(x):
    x = int(x)
    return render_template("index.html", 
                            x=x,
                            eval = eval)
