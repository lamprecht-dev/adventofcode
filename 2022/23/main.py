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
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    elves = {}

    ll = lines(d)
    for row in range(len(ll)):
        for col in range(len(ll[0])):
            if ll[row][col] == "#":
                elves[(row, col)] = (0, None) # Pos, cycle, target | cycle needs to go -= 1

    dirs = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1),
            "NE": (-1, 1), "NW": (-1, -1), "SE": (1, 1), "SW": (1, -1)}
    counter = 0
    while True:
        elves_moved = False
        counter += 1
        positions = set()
        for pos, elf in elves.items():
            positions.add(pos)

        # Select target
        for pos, elf in elves.items():
            neighbors = [dirs["N"], dirs["NE"], dirs["NW"], dirs["S"], dirs["SE"], dirs["SW"], dirs["W"], dirs["E"]]
            has_neighbors = False
            for n in neighbors:
                n_pos = [sum(x) for x in zip(n, pos)]
                if tuple(n_pos) in positions:
                    has_neighbors = True
                    break

            if not has_neighbors:
                continue

            for i in range(4):
                if i == elf[0] % 4:
                    p_dirs = [dirs["N"], dirs["NE"], dirs["NW"]]
                    w_dir = dirs["N"]
                elif i == (elf[0] + 1) % 4:
                    p_dirs = [dirs["S"], dirs["SE"], dirs["SW"]]
                    w_dir = dirs["S"]
                elif i == (elf[0] + 2) % 4:
                    p_dirs = [dirs["W"], dirs["NW"], dirs["SW"]]
                    w_dir = dirs["W"]
                else:
                    p_dirs = [dirs["E"], dirs["NE"], dirs["SE"]]
                    w_dir = dirs["E"]

                in_general_direction = False
                for p in p_dirs:
                    n_pos = [sum(x) for x in zip(pos, p)]
                    n_pos = tuple(n_pos)
                    if n_pos in positions:
                        in_general_direction = True
                        break
                if in_general_direction:
                    continue

                new_pos = [sum(x) for x in zip(w_dir, pos)]
                elves[pos] = (elf[0], tuple(new_pos))
                break

        targets = coll.defaultdict(int)
        for pos, elf in elves.items():
            targets[elf[1]] += 1

        new_elves = {}
        for pos, elf in elves.items():
            if elf[1] is None or targets[elf[1]] > 1:
                new_elves[pos] = ((elf[0] - 1) % 4, None)
                continue
            elves_moved = True
            new_elves[elf[1]] = ((elf[0] - 1) % 4, None)

        elves = new_elves

        min_col = math.inf
        min_row = math.inf
        max_col = -math.inf
        max_row = -math.inf
        for (row, col) in elves:
            min_col = min(min_col, col)
            min_row = min(min_row, row)
            max_col = max(max_col, col)
            max_row = max(max_row, row)

        for row in range(max_row - min_row + 1):
            row_string = ""
            for col in range(max_col - min_col + 1):
                if (row + min_row, col + min_col) in elves:
                    row_string += "#"
                else:
                    row_string += "."
        #     print(row_string)
        # print()
        if not elves_moved:
            break

        if counter == 11:
            t = (max_row - min_row + 1) * (max_col - min_col + 1) - len(elves)
    t2 = counter

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
#     s = """.....
# ..##.
# ..#..
# .....
# ..##.
# ....."""
    a1 = 110
    a2 = 20
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



