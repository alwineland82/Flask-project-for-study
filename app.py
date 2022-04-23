from flask import Flask, render_template


app = Flask(__name__)

def boo(x, y):
    return x + y


@app.route('/')
def index():
    return render_template("index.html", boo=boo)
