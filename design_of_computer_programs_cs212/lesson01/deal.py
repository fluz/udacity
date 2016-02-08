"""
Check the distribution of cards in a hand (in a poker game)
"""
from __future__ import division
import random
import poker_game


MY_DECK = [r+s for r in '23456789TJQKA' for s in 'SHDC']


def deal(num_hands, n=5, deck=MY_DECK):
    """ Generate a number num_hands to analise the distribution of ranked ranks in a distribution
    """
    diff_hands = []
    for i in xrange(num_hands):
        hand = [random.choice(deck) for x in xrange(n)]
        diff_hands.append(hand)

    return diff_hands



if __name__ == "__main__":
    print deal(2)
