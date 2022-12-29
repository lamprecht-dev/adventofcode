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

    def move(self, dir, spots):
        if not(0 <= self.col + dir[0] <= 7 - self.w) or self.row + dir[1] < 0 or self.does_collide(dir, spots):
            if dir is self.DOWN:
                self.settled = True
            return False

        self.col += dir[0]
        self.row += dir[1]

        return True

    def does_collide(self, dir, spots):
        coords = self.get_coords(dir)
        for c in coords:
            if c in spots:
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


rep_saver = []
save_tops = []
def process_repetition(profile, type, cycle):
    np = normalize_profile(profile)
    n = (np, type, cycle)
    if n in rep_saver:
        ind = rep_saver.index(n)
        return ind, save_tops[ind]
    rep_saver.append(n)
    save_tops.append(profile.copy())
    return None, None


def normalize_profile(p):
    min_val = math.inf
    for val in p:
        min_val = min(min_val, val)

    normalized = tuple([(x - min_val) for x in p])
    return normalized


def get_height(profile):
    max_val = -math.inf
    for val in profile:
        max_val = max(max_val, val)
    return max_val


def solve(data):
    stats(data)
    print("Input: ", repr(data))
    t = -1

    UsedSpots = set()
    top_profile = [-1 for _ in range(7)]
    ty = 0
    di = 0
    answer = -1
    repeat_at = -1
    repeat_to = -1
    amnt = -1
    diff = -1
    target = 1000000000000
    time = 0
    top_diff = 0
    top_adjust = 0
    while time < target:
        s = Shape(ty, t + 4)
        ty += 1
        if ty >= 5:
            ty = 0
        while not s.settled:
            dir = Shape.LEFT if data[di] == "<" else Shape.RIGHT
            s.move(dir, UsedSpots)
            di += 1
            if len(data) <= di:
                di = 0
            if not s.move(Shape.DOWN, UsedSpots):
                t = max(s.top(), t)

        coords = s.get_coords()
        for c in coords:
            UsedSpots.add(c)
            top_profile[c[0]] = max(top_profile[c[0]], c[1])

        if repeat_at == -1:
            repat, old_top = process_repetition(top_profile, ty, di)
            if repat is not None and time > 2022:
                repeat_at = repat
                repeat_to = time
                diff = repeat_to - repeat_at
                amnt = (target - time) // diff
                top_diff = get_height(top_profile) - (get_height(old_top))
                time = time + diff * amnt - 1
                top_adjust = top_diff * amnt

        if time == 2022:
            answer = t

        time += 1
    print(top_adjust, t, top_diff, amnt, time, diff)
    return answer - 1, get_height(top_profile) + top_adjust

# Tried answers
# 1536994219669  should be the answer but still not getting it... again test is correct
# 1594124700129 too high
# 1594124700130 too high


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
    a1 = 3068
    a2 = 1514285714288
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



