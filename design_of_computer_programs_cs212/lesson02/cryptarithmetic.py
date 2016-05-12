# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the
# program is incomplete. Please SUBMIT to see if you are correct.

from __future__ import division
import string
from itertools import permutations
import re


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(formula) & set(string.uppercase))  # should be a string
    for digits in permutations(string.digits, len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    "Formula f is valid if it has no number with leading zero and evals true"
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    #  Super class for ZeroDivisionError
    except ArithmeticError:
        return False
