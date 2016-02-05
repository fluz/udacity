

def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable"""
    result, maxval = [], None
    key = key or (lambda x: x)
    for i in iterable:
        if len(result) == 0 or maxval < key(i):
            result, maxval = [i], key(i)
            print result
        elif maxval == key(i):
            result.append(i)
    return result


def hand_rank(hand):
    """define a rank for a specific hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def card_ranks(cards):
    """ Return a list of the ranks, sorted with higher first"""
    ranks = ["--23456789TJQKA".index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    """ Return True if the ordered ranks from a 5 card straight"""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """ Return True if all cards have the same suit"""
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """ Return the first rank that this hand has exactly n
        and return None otherwise"""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
       tuple: (highest, lowest); otherwise return None."""
    pair_highest = kind(2, ranks)
    pair_lowest = kind(2, list(reversed(ranks)))
    if pair_highest and pair_highest != pair_lowest:
        return (pair_highest, pair_lowest)
    return None
