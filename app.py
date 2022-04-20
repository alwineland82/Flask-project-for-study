from flask import Flask, render_template


app = Flask(__name__)

@app.route('/<x>/')
def index(x):
    x = float(x)
    pi = 3.14
    return render_template("index.html", 
                            text=f"Circle area = {x ** 2 * pi}")
