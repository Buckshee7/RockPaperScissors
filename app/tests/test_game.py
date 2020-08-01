import unittest
from app.modules.player import Player
from app.modules.game import play_game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Tim", "Rock")
        self.player_2 = Player("Ally", "Paper")
        self.player_3 = Player("Jarrod", "Scissors")

    def test_same_choice(self):
        self.assertEqual(None, play_game(self.player_1, self.player_1))

    def test_rock_paper(self):
        self.assertEqual(self.player_2, play_game(self.player_1, self.player_2))

    def test_rock_scissors(self):
        self.assertEqual(self.player_1, play_game(self.player_1, self.player_3))
    
    def test_lava_scissors(self):
        player_4 = Player("Cheater", "Lava")
        self.assertEqual(player_4, play_game(player_4, self.player_3))

    def test_rock_lava(self):
        player_4 = Player("Cheater", "Lava")
        self.assertEqual(player_4, play_game(self.player_1, player_4))

    