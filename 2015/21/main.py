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


def simulate(you, boss):
    u_atk = max(1, you[1] - boss[2])
    b_atk = max(1, boss[1] - you[2])
    u_time = math.ceil(boss[0] / u_atk)
    b_time = math.ceil(you[0] / b_atk)
    return u_time <= b_time


def get_you(itms):
    dmg = 0
    arm = 0
    cost = 0
    counts = [0, 0, 0]
    for i in itms:
        cost += i[1]
        dmg += i[2]
        arm += i[3]
        counts[i[0]] += 1
    return (100, dmg, arm), cost, (counts[0] == 0, counts[1] == 0, counts[2] < 2)


def win(itms, boss):
    # Not enough arguments to warrant Dijkstra's
    you, cost, can_buys = get_you(itms)
    if simulate(you, boss) and not can_buys[0]:
        return cost

    best = math.inf
    for i in items:
        if i in itms or not can_buys[i[0]]:
            continue
        best = min(best, win(itms + [i], boss))

    return best


def loose(itms, boss):
    you, cost, can_buys = get_you(itms)
    won = simulate(you, boss)
    if won:
        return 0  # We cant loose anymore even if we buy more

    if not won and len(itms) == 4:
        return cost  # dead end as we have all items

    best = 0
    if not won and not can_buys[0]: # Here is the little hickup. I need to buy a weapon! Important detail
        best = cost
    for i in items:
        if i in itms or not can_buys[i[0]]:
            continue
        best = max(best, loose(itms + [i], boss))

    return best  # 233 too high   # not 141


items = [(0, 8, 4, 0), (0, 10, 5, 0), (0, 25, 6, 0), (0, 40, 7, 0), (0, 74, 8, 0), (1, 13, 0, 1), (1, 31, 0, 2),
         (1, 53, 0, 3), (1, 75, 0, 4), (1, 102, 0, 5), (2, 25, 1, 0), (2, 50, 2, 0), (2, 100, 3, 0),
         (2, 20, 0, 1), (2, 40, 0, 2), (2, 80, 0, 3)]


def solve(d):
    ww = words(d)
    boss = tuple(ints((ww[0][2], ww[1][1], ww[2][1])))  #hp, dmg, arm

    t = win([], boss)
    t2 = loose([], boss)

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
