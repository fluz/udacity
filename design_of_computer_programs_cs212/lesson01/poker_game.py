

def poker(hands):
    """Return the best hand: poker([hand,...]) => hand"""
    return max(hands, key=hand_rank)


def hand_rank(hand):
    """define a rank for a specific hand"""
    return None  # we will be changing this later.
