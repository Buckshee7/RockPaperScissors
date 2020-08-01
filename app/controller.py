from app import app
from flask import render_template, request, redirect
from app.modules.game import play_game, generate_computer_player
from app.modules.player import Player

@app.route('/')
def index(player_name = ""):
    return render_template('index.html', player_name = player_name, title = "Play New Game!")

@app.route('/<choice_1>/<choice_2>')
def play_new_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1.capitalize())
    player_2 = Player("Player 2", choice_2.capitalize())
    winner = play_game(player_1, player_2)
    return render_template('result.html', player_1 = player_1, player_2 = player_2, winner = winner)

@app.route('/play')
def get_choice():
    return render_template('vscomp.html')

@app.route('/vscomp', methods=['POST'])
def play_against_computer():
    choice = request.form['choice']
    name = request.form['name']
    human = Player(name, choice)
    computer = generate_computer_player()
    winner = play_game(human, computer)
    return render_template('result.html', player_1 = human, player_2 = computer, winner = winner)
    
    
    