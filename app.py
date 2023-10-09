from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET KEY'] = "pineapple24"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = list()

@app.route('/')
def home_page():
    return render_template("home.html")

    

