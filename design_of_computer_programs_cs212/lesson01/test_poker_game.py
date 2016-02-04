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
            poker_game.poker([fk, sf, fh]), sf)
        self.assertEqual(poker_game.poker([fk, fh]), fk)
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

    def test_flush(self):
        """ Test the flush """
        sf = "6C 7C 8C 9C TC".split()
        fk = "9D 9H 9S 9C 7D".split()

        self.assertEqual(poker_game.flush(sf), True)
        self.assertEqual(poker_game.flush(fk), False)

    def test_straight(self):
        """ Test the straight """

        self.assertEqual(poker_game.straight([9, 8, 7, 6, 5]), True)
        self.assertEqual(poker_game.straight([9, 8, 7, 4, 5]), False)

    def test_kind(self):
        """ Test the kind """
        fk = "9D 9H 9S 9C 7D".split()

        fkranks = poker_game.card_ranks(fk)

        self.assertEqual(poker_game.kind(4, fkranks), 9)
        self.assertEqual(poker_game.kind(3, fkranks), None)
        self.assertEqual(poker_game.kind(2, fkranks), None)
        self.assertEqual(poker_game.kind(1, fkranks), 7)

    def test_two_pair(self):
        """ Test two pairs"""
        fk = "9D 9H 9S 9C 7D".split()
        tp = "TD 9H TH 7C 7S".split()
        fkranks = poker_game.card_ranks(fk)
        tpranks = poker_game.card_ranks(tp)

        print fkranks
        print tpranks

        self.assertEqual(poker_game.two_pair(fkranks), None)
        self.assertEqual(poker_game.two_pair(tpranks), (10, 7))
