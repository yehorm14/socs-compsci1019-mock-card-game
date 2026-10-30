import unittest
from unittest.mock import patch
from card_game.card.entity.Deck import *


class TestMockDeck(unittest.TestCase):

    @patch("card_game.card.entity.Deck.random.randint")
    def test_play_a_card_from_deck_random(self, mock_randint):
        # Sub-task 5 – Mock Random Card Selection
        mock_randint.return_value = 0
        deck = create_deck()
        first_card = deck[0]

        card = play_a_card_from_deck(deck)

        self.assertEqual(card, first_card)
        mock_randint.assert_called_once_with(0, 51)