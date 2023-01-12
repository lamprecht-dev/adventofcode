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

class Cell:
    def __init__(self, state, x, y, stuck=False):
        self.state = state == "#"
        self.x, self.y = x, y
        self.trigger_state = False
        self.stuck = stuck

    def trigger(self, States):
        if self.stuck:
            self.trigger_state = True
            return
        count_neighbors = 0
        for yi in range(3):
            for xi in range(3):
                ny = yi + self.y - 1
                nx = xi + self.x - 1
                if ny < 0 or nx < 0 or ny >= len(States) or nx >= len(States[0]) or yi == xi == 1:
                    continue
                count_neighbors += int(States[ny][nx].state)

        if self.state:
            if count_neighbors == 2 or count_neighbors == 3:
                self.trigger_state = True
            else:
                self.trigger_state = False
        else:
            if count_neighbors == 3:
                self.trigger_state = True
            else:
                self.trigger_state = False

    def switch(self):
        self.state = self.trigger_state


def solve(d):
    t = 0
    t2 = 0

    G = []

    ll = lines(d)
    for r in range(len(ll)):
        row = []
        for c in range(len(ll[0])):
            row.append(Cell(ll[r][c], c, r))
        G.append(row)

    for _ in range(100):
        cur_count = 0
        for gg in G:
            for g in gg:
                g.trigger(G)
                cur_count += int(g.state)

        for gg in G:
            for g in gg:
                g.switch()

    for gg in G:
        for g in gg:
            t += int(g.state)

    # Part 2
    G = []

    ll = lines(d)
    for r in range(len(ll)):
        row = []
        for c in range(len(ll[0])):
            stuck = False
            if (r, c) in [(0, 0), (0, 99), (99, 99), (99, 0)]:
                stuck = True
            row.append(Cell(ll[r][c], c, r, stuck))
        G.append(row)

    for _ in range(100):
        cur_count = 0
        for gg in G:
            for g in gg:
                g.trigger(G)
                cur_count += int(g.state)

        for gg in G:
            for g in gg:
                g.switch()

    for gg in G:
        for g in gg:
            t2 += int(g.state)

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()

