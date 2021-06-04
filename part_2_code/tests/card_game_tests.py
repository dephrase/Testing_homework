import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()

    def test_card_is_ace(self):
        self.card1 = Card("Hearts", 1)
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def highest_card_is_returned(self):
        self.card1 = Card("Spades", 7)
        self.card2 = Card("Hearts", 8)
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))
