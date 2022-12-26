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


def get_bliz_pos(b, t, w, h):
    if b[2] == ">":
        p = b[0], b[1] + t
    elif b[2] == "<":
        p = b[0], b[1] - t
    elif b[2] == "^":
        p = b[0] - t, b[1]
    else:
        p = b[0] + t, b[1]

    while p[0] < 1:
        p = (p[0] + (h - 2)), p[1]
    while p[0] >= h - 1:
        p = (p[0] - (h - 2)), p[1]
    while p[1] < 1:
        p = p[0], (p[1] + (w - 2))
    while p[1] >= w - 1:
        p = p[0], (p[1] - (w - 2))
    return p


def get_blitz_pos_all(B, t, DP, w, h):
    t = t % (w * h)
    if t not in DP:
        DP[t] = set()
        for b in B:
            DP[t].add(get_bliz_pos(b, t, w, h))

    return DP


def solve(d):
    stats(d)
    print("Input: ", repr(d))

    ll = lines(d)
    w = len(ll[0])
    h = len(ll)

    entrance = ()
    exit = ()
    B = []
    DP = {}

    for row in range(len(ll)):
        for col in range(len(ll[row])):
            if row == 0 and ll[row][col] == ".":
                entrance = (row, col)
            elif row == h - 1 and ll[row][col] == ".":
                exit = (row, col)

            if h > row > 0 and w > col > 0:
                if ll[row][col] not in  [".", "#"]:
                    B.append((row, col, ll[row][col]))

    for t in range(w * h + 2):
        print(t, w, h, w*h)
        DP = get_blitz_pos_all(B, t, DP, w, h)

    # 3D BFS where the z axis is time
    next = [(*entrance, 0)]
    his = {(*entrance, 0): []}
    done = []
    # Priorotized by the ones that actually get us closer
    dirs = {"d": (1, 0, 1), "r": (0, 1, 1), "n": (0, 0, 1), "l": (0, -1, 1), 'u': (-1, 0, 1)}


    t = 0
    while len(next) > 0:
        c = next.pop(0)
        print(c)
        row, col, t = c

        if (row, col) == exit:
            break  # Done

        BPos = DP[t + 1]

        for _, d in dirs.items():
            nt = t + d[2]
            n_pos = (row + d[0], col + d[1], nt)

            if n_pos in done or n_pos in next:
                continue

            if not(0 < n_pos[0] < h and 0 < n_pos[1] < w) and not (*entrance, nt) == n_pos and not (*exit, nt) == n_pos:
                continue  # Wall but entrance and exit is allowed

            if (n_pos[0], n_pos[1]) in BPos:
                continue  # Blizzard at that time

            his[n_pos] = his[c] + [c]

            next.append(n_pos)

        done.append(c)

    return t, 0


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
    a1 = 18
    a2 = 0
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()


