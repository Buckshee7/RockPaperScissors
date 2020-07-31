from app import app
from flask import render_template, request, redirect
from app.modules.game import play_game
from app.modules.player import Player

@app.route('/')
def index(player_name = ""):
    return render_template('index.html', player_name = player_name, title = "Play New Game!")

@app.route('/<choice_1>/<choice_2>')
def play_new_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1.capitalize())
    player_2 = Player("Player 2", choice_2.capitalize())
    winner = play_game(player_1, player_2)
    return render_template('result.html', winner = winner)