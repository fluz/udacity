""" Tester for poker_game.py"""


import unittest
import poker_game


class TddPokerGame(unittest.TestCase):
    """ Class to test poker game program"""

    def test_case(self):
        """ doc """

        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()
        fh = "TD TC TH 7C 7D".split()

        self.assertEqual(poker_game.poker([sf, fh, fk]), sf)
        self.assertEqual(poker_game.poker([fh, fk]), fh)
        self.assertEqual(poker_game.poker([fk]), fk)
        self.assertEqual(poker_game.poker([sf]+[fk]*99), sf)
