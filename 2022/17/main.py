import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq

from utils import *


class Shape:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, -1)

    def __init__(self, type, row):
        self.row = row
        self.col = 2
        self.type = type
        self.settled = False

        if type == 0:
            self.P = [(0, 0), (1, 0), (2, 0), (3, 0)]   # -
            self.w = 4
        elif type == 1:
            self.P = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]  # +
            self.w = 3
        elif type == 2:
            self.P = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]  # _|
            self.w = 3
        elif type == 3:
            self.P = [(0, 0), (0, 1), (0, 2), (0, 3)]  # I
            self.w = 1
        else:
            self.P = [(0, 0), (0, 1), (1, 0), (1, 1)]  # o
            self.w = 2

    def move(self, dir, S):
        if not(0 <= self.col + dir[0] <= 7 - self.w) or self.row + dir[1] < 0 or self.does_collide(dir, S):
            if dir is self.DOWN:
                self.settled = True
            return False

        self.col += dir[0]
        self.row += dir[1]

        return True

    def does_collide(self, dir, S):
        S_lim = S[-100:]
        for s in S_lim:
            if self.check_collision(dir, s):
                return True
        return False

    def check_collision(self, dir, s):
        P1 = self.get_coords(dir)
        P2 = s.get_coords()

        for p in P1:
            if p in P2:
                return True

        return False

    def get_coords(self, rel=(0, 0)):
        C = []
        for p in self.P:
            C.append((p[0] + self.col + rel[0], p[1] + self.row + rel[1]))
        return C

    def top(self):
        m = 0
        for p in self.P:
            m = max(m, p[1])
        return m + self.row

def solve(d):
    stats(d)
    print("Input: ", repr(d))
    t = -1
    t2 = 0

    S = []
    ty = 0
    di = 0
    for _ in range(2):
        s = Shape(ty, t + 4)
        ty += 1
        if ty >= 5:
            ty = 0
        while not s.settled:
            dir = Shape.LEFT if d[di] == "<" else Shape.RIGHT
            s.move(dir, S)
            di += 1
            if len(d) <= di:
                di = 0
            if not s.move(Shape.DOWN, S):
                t = max(s.top(), t)

        S.append(s)

    C = set()

    for s in S:
        for p in s.get_coords():
            C.add(p)

    for r in range(t + 1):
        s = ""
        for c in range(1, 8):
            if (c - 1, t - r) in C:
                s += "#"
            else:
                s += "."
        print(s)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
    a1 = 3068
    a2 = 0
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



