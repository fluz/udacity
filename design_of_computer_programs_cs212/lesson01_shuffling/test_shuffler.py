"""Testing the diverses algorithms to shuffler."""
from collections import defaultdict
from random import randrange


def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in xrange(n):
        input = list(deck)
        shuffler(input)
        counts["".join(input)] += 1
    e = n * 1. / factorial(len(deck))  # expected value
    ok = all((0.9 <= counts[item] / e <= 1.1) for item in counts)
    name = shuffler.__name__
    print("{0}({1}) {2}").format(name, deck, ("ok" if ok else "**** BAD ****"))
    print "    ",
    for item, count in sorted(counts.items()):
        print("{0}:{1:4.1f}").format(item, count * 100. / n)
    print


def factorial(n): return 1 if (n <= 1) else n * factorial(n - 1)


def shuffle(deck):
    "Knuth's algorithm P"
    N = len(deck)
    for i in xrange(N-1):
        swap(deck, i, randrange(i, N))


def shuffle1(deck):
    "Teacher's of Peter algorithm"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle2(deck):
    "modifified version of shuffle 1"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):
    "Another modification in shuffle 1"
    N = len(deck)
    for i in xrange(N):
        swap(deck, i, randrange(N))


def swap(deck, i, j):
    "Swap elements i and j of a collection"
    deck[i], deck[j] = deck[j], deck[i]


def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc', 'ab', 'abcd']):
    "compare the shufflers"
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)


def main():
    test_shufflers([shuffle, shuffle1, shuffle2, shuffle3])


if __name__ == "__main__":
    main()
