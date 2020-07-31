from player import Player

def play_game(player_1, player_2):
    if player_1.choice == player_2.choice:
        return "draw"
    elif player_1.choice == "rock":
        if player_2.choice == "paper":
            return player_2
    elif player_1.choice == "paper":
        if player_2.choice == "scissors:":
            return player_2
    elif player_1.choice == "scissors"
        if player_2.choice == "rock":
            return player_2
    else:
        return player_1