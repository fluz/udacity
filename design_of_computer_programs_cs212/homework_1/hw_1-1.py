from itertools import combinations
import sys
sys.path.insert(0, '../lesson01/')
from poker_game import poker

def best_seven_cards(hand):
	hand_combinations = list(combinations(hand, 5))
	print poker(hand_combinations)


def main():
	hands = []
	hands.append("AS AC AH KS AD KD KH".split())
	for hand in hands:
		best_seven_cards(hand)


if __name__ == "__main__":
	main()