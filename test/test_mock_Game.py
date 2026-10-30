import unittest
from unittest.mock import patch, mock_open
from card_game.Game import *

class test_mock_Game(unittest.TestCase):

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_game_info(self, mock_get_string):
        #Sub-task 2 – Mock Console Game Info
        mock_get_string.side_effect = ["Derek", "3"]

        name, number_of_players = get_game_info()

        self.assertEqual(name, "Derek")
        self.assertEqual(number_of_players, 3)
        

    def test_get_computer_players_names(self):
        #Sub-task 5 – Mock Get Player Names
        pass