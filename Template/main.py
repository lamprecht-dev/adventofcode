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

# TODO: CREATE CLASSES FOR VM, Tree, Graph etc


def solve(d):
    stats(d)
    # print("Input: ", repr(d))
    t = 0
    t2 = 0

    # nums = ints(d)

    # ww = words(d)
    # for line in ww:
    #     for word in line:

    # for line in d.split("\n"):
    #     for w in line.split():
    #         print(w)

    # nums = [int(x) for x in d.split("\t")]
    # nums = [[int(x) for x in l.split("\t")] for l in d.split("\n")]
    # for num in nums:

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """"""
    a1 = 0
    a2 = 0
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



