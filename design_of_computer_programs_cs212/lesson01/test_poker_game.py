""" Tester for poker_game.py"""


import unittest
import poker_game


class TddPokerGame(unittest.TestCase):
    """ Class to test poker game program"""

    def test_winner(self):
        """ Test the return of the best hand """
        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()
        fh = "TD TC TH 7C 7D".split()

        self.assertEqual(
            poker_game.poker([fk, sf, fh]), fh)
        self.assertEqual(poker_game.poker([fk, fh]), fh)
        self.assertEqual(poker_game.poker([fk, fk]), fk)
        self.assertEqual(poker_game.poker([fk]), fk)
        self.assertEqual(poker_game.poker([fk] * 99 + [sf]), sf)

    def test_hand_rank(self):
        """ Test the output of a hand_rank"""

        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()
        fh = "TD TC TH 7C 7D".split()

        self.assertEqual(poker_game.hand_rank(sf), (8, 10))
        self.assertEqual(poker_game.hand_rank(fk), (7, 9, 7))
        self.assertEqual(poker_game.hand_rank(fh), (6, 10, 7))

    def test_card_ranks(self):
        """ Test the card ranks"""
        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()
        fh = "TD TC TH 7C 7D".split()

        self.assertEqual(poker_game.card_ranks(sf), [10, 9, 8, 7, 6])
        self.assertEqual(poker_game.card_ranks(fk), [9, 9, 9, 9, 7])
        self.assertEqual(poker_game.card_ranks(fh), [10, 10, 10, 7, 7])
