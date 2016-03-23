import string
import re


def valid(f):
    "Formula f is valid if it has no number with leading zero and evals true"
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ZeroDivisionError:
        return False
