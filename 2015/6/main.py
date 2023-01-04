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
    t = 0
    t2 = 0

    G = [[False for _ in range(1000)] for _ in range(1000)]
    G2 = [[0 for _ in range(1000)] for _ in range(1000)]

    ww = words(d)
    for line in ww:
        if line[0] == "toggle":
            r1, c1 = ints(line[1], ",")
            r2, c2 = ints(line[3], ",")
            for nr in range(r1, r2 + 1):
                for nc in range(c1, c2 + 1):
                    G[nr][nc] = not G[nr][nc]
                    G2[nr][nc] += 2
        else:
            r1, c1 = ints(line[2], ",")
            r2, c2 = ints(line[4], ",")
            for nr in range(r1, r2 + 1):
                for nc in range(c1, c2 + 1):
                    G[nr][nc] = line[1] == "on"
                    G2[nr][nc] += int(line[1] == "on") * 2 - 1
                    if G2[nr][nc] < 0:
                        G2[nr][nc] = 0

    for r in G:
        for c in r:
            t += c is True

    for r in G2:
        for c in r:
            t2 += c

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



