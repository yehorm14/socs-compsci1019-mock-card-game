import unittest
from unittest.mock import patch
from card_game.communication.ConsoleInOut import *

class test_mock_ConsoleInOut(unittest.TestCase):

    def test_get_input_string(self, mock_input):
        pass

    @patch('card_game.communication.ConsoleInOut.get_string')
    def test_get_input_integer(self, mock_get_string):
        #Sub-task 1: Mock Console Input Integer
        mock_get_string.return_value = "18"
        self.assertEqual(get_input_integer("Enter a number"), 18)

    def test_get_input_string_builtin(self):
        pass

    def test_get_integer_max_attempts(self):
        #Sub-task 3 – Mock Console Input With Built In
        pass

    def test_get_input_integer_builtin(self):
        pass