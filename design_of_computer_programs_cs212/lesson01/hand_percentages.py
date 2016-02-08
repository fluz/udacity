""" Check the distribution in a poker game"""
from __future__ import division
import deal
import poker_game


def hand_percentages(n_hands=700*1000):
    """
      Sample n_hands random and print a table of percentages for each type of hand
    """
    label = ["Higer card", "One pair", "Two pairs", "Three of a kind",
             "Straight", "Flush", "Full House", "Four of a kind", "Straight Flush"]
    counts = [0]*9

    for i in xrange(n_hands//10):
        for hand in deal.deal_2(10):
            ranking = poker_game.hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(xrange(9)):
        print "{0:14s} {1:6.3f} %".format(label[i], 100.*counts[i]/n_hands)


if __name__ == "__main__":
    hand_percentages()
