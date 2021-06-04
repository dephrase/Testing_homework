import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame("CardGame")

    def test_card_is_ace(self):
        self.card1 = Card("Hearts", 1)
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_card_is_not_ace(self):
        self.card1 = Card("Hearts", 5)
        self.assertEqual(False, self.cardgame.check_for_ace(self.card1))

    def test_highest_card_is_returned(self):
        self.card1 = Card("Spades", 7)
        self.card2 = Card("Hearts", 8)
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    def test_cardstotal_returns_total_value_of_two_cards(self):
        self.card1 = Card("Spades", 7)
        self.card2 = Card("Hearts", 8)
        self.cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 15", self.cardgame.cards_total(self.cards))