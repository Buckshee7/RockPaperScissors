from app.modules.player import Player
import random

def play_game(player_1, player_2):
    if player_1.choice == player_2.choice:
        return
    elif player_1.choice == "Rock" and player_2.choice == "Paper":
            return player_2
    elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            return player_2
    elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return player_2
    else:
        return player_1

def generate_computer_player():
    choices = ["Rock", "Paper", "Scissors"]
    choice = choices[random.randint(0,len(choices)-1)]
    return Player("Computer", choice)