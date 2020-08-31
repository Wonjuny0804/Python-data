import string
import collections

from deque import Deque

STRIP = string.whitespace + string.punctuation + "\"'"

def palindrome_checker_with_deque(str1):
    d1 = Deque()
    d2 = collections.deque()

    for s in str1.lower():
        if s not in STRIP:
            d2.append(s)
            d1.enqueue(s)

    