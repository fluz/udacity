from itertools import combinations
import sys
sys.path.insert(0, '../lesson01/')
from poker_game import poker, hand_rank


def best_seven_cards(hand):
    return max(list(combinations(hand, 5)), key=hand_rank)


def main():
    hands = []
    hands.append("AS AC AH KS AD KD KH".split())
    for hand in hands:
        print best_seven_cards(hand)


if __name__ == "__main__":
    main()
