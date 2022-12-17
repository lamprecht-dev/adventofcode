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


def solve(d):
    stats(d, " -> ")
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    G = Grid(default_value=" ")

    ww = words(d, " -> ")
    for line in ww:
        from_coord = None
        to_coord = None
        for word in line:
            if from_coord is not None:
                to_coord = from_coord
            from_coord = ints(word.split(','))

            if to_coord is not None:
                diff_coord = [abs(from_coord[0] - to_coord[0]), abs(from_coord[1] - to_coord[1])]
                dir_coord = [(from_coord[0] - to_coord[0]) // diff_coord[0] if diff_coord[0] != 0 else 0,
                             (from_coord[1] - to_coord[1]) // diff_coord[1] if diff_coord[1] != 0 else 0]

                for i in range(max(diff_coord) + 1):
                    if diff_coord[0] == 0:
                        G.set(from_coord[0], to_coord[1] + i * dir_coord[1], "█")
                    else:
                        G.set(to_coord[0] + i * dir_coord[0], from_coord[1], "█")

    bottom_line = G.h
    sand_hit_bottom = False
    sand_stopped_flowing = False
    while not sand_stopped_flowing:
        sand_pos = (500, -1)
        sand_moved = True
        while sand_moved:
            if sand_pos[1] == bottom_line:
                sand_hit_bottom = True
                G.set(sand_pos[0], sand_pos[1], "░")
                t2 += 1
                break
            if G.get(sand_pos[0], sand_pos[1] + 1) == " ":
                sand_pos = (sand_pos[0], sand_pos[1] + 1)
            elif G.get(sand_pos[0] - 1, sand_pos[1] + 1) == " ":
                sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
            elif G.get(sand_pos[0] + 1, sand_pos[1] + 1) == " ":
                sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            else:
                G.set(sand_pos[0], sand_pos[1], "░")
                sand_moved = False
                if not sand_hit_bottom:
                    t += 1
                t2 += 1
                if sand_pos == (500, 0):
                    sand_stopped_flowing = True

    # print(G.get_non_default_values())
    G.literal_print()

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    a1 = 24
    a2 = 93
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



