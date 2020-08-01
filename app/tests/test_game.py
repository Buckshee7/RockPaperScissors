import unittest
from app.modules.player import Player
from app.modules.game import play_game, generate_computer_player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Tim", "Rock")
        self.player_2 = Player("Ally", "Paper")
        self.player_3 = Player("Jarrod", "Scissors")
        self.player_4 = Player("Cheater", "Lava")


    def test_same_choice(self):
        self.assertEqual(None, play_game(self.player_1, self.player_1))

    def test_rock_paper(self):
        self.assertEqual(self.player_2, play_game(self.player_1, self.player_2))

    def test_rock_scissors(self):
        self.assertEqual(self.player_1, play_game(self.player_1, self.player_3))
    
    def test_lava_scissors(self):
        self.assertEqual(self.player_4, play_game(self.player_4, self.player_3))

    def test_rock_lava(self):
        self.assertEqual(self.player_4, play_game(self.player_1, self.player_4))

    # Computer should pick rock/paper/scissors @ 30% and lava @ 10%
    def test_generate_computer_player(self):
        thousand_computers = []
        for i in range(1000):
            thousand_computers.append(generate_computer_player())
        thousand_choices = []
        for computer in thousand_computers:
            thousand_choices.append(computer.choice)
        rocks = thousand_choices.count("Rock")
        papers = thousand_choices.count("Paper")
        scissors = thousand_choices.count("Scissors")
        lavas = thousand_choices.count("Lava")

        self.assertAlmostEqual(300, rocks, delta = 30)
        self.assertAlmostEqual(300, papers, delta = 30)
        self.assertAlmostEqual(300, scissors, delta = 30)
        self.assertAlmostEqual(100, lavas, delta = 10)