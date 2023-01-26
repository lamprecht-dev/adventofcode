import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq
# import sys
# sys.setrecursionlimit(1000000)

from utils import *


def solve(d):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    # nums = ints(d)

    # ll = lines(d)
    # for line in ll:

    # ww = words(d)
    # for line in ww:


    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

main()
