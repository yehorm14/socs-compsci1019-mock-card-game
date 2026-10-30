import unittest
from unittest.mock import patch, mock_open
from card_game.LoadCSV import *

class test_mock_LoadCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="Derek\nXi")
    def test_get_csv_rows(self, mock_file):
        #Sub-task 4 – Mock File Load
        rows = get_csv_rows("any_file.csv")

        self.assertEqual(rows[1][0], "Xi")
        
        