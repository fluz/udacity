# -------------
# User Instructions
#
# Tester for cryptarithimetic.py
#

from cryptarithmetic import solve
from time_measure import timedcall
import time

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == CY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test():
    t0 = time.clock()
    for example in examples:
        print("")
        print(13*" "), example
        r = timedcall(solve, example)
        print("{0:8.6f} sec:    {1}".format(r[0],r[1]))
    print "{0:8.6f} tot.".format(time.clock()-t0)


if __name__ == "__main__":
    test()
