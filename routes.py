
from . import app
from flask import render_template


@app.route('/')
def hello_world():
    return "hello world from flask"

@app.route('/character/new')
def character_new():
    #generate new character
    character = None
    return render_template("character_new.html", character=character)


@app.route('synthwave/')
def main():
    return render_template("synthwave.html")
