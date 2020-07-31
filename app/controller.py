from app import app
from flask import render_template, request, redirect
from app.modules.game import play_game
from app.modules.player import Player

@route('/')
def index(player_name = ""):
    return render_template('index.html', player_name = player_name, title = "Play New Game!")

