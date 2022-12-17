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


def valid(x, y, S):
    for (sx, sy, d) in S:
        dxy = abs(sx - x) + abs(sy - y)
        if dxy <= d:
            return False
    return True


def solve(d, is_test=False):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    S = []
    B = []
    blocked = set()

    for ll in lines(d):
        ll = ll.replace('Sensor at ', '').replace('x=', '').replace(' y=', '').split(': closest beacon is at ')
        signal = None

        for i in ll:
            nums = ints(i, ",")
            if signal is None:
                signal = nums
            else:
                diff = nums[0] - signal[0], nums[1] - signal[1]
                dist = abs(diff[0]) + abs(diff[1])
                S.append((signal[0], signal[1], dist))
                B.append(tuple(nums))

                check_row = 2000000 if not is_test else 10

                row_distance = abs(check_row - signal[1])

                if dist < row_distance:
                    continue

                block_amount = dist - row_distance
                for i in range(block_amount + 1):
                    b1 = signal[0] + i, check_row
                    b2 = signal[0] - i, check_row
                    blocked.add(b1)
                    blocked.add(b2)

    for b in B:
        if b in blocked:
            blocked.remove(b)
    t = len(blocked)

    for (sx, sy, d) in S:
        # Go along the outside of the square and check if valid
        for i in range(d * 2 + 3):
            dx = i - d - 1
            dy = abs(abs(dx) - d - 1)

            x = sx + dx
            y1 = sy + dy
            y2 = sy - dy

            assert abs(x - sx) + abs(y1 - sy) == d + 1
            assert abs(x - sx) + abs(y2 - sy) == d + 1

            max_distance = 4000000 if not is_test else 20

            if valid(x, y1, S) and 0 <= x <= max_distance and 0 <= y1 <= max_distance:
                print(sx, sy, dx, dy, d, x, y1)
                return t, x * 4000000 + y1
            if valid(x, y2, S) and 0 <= x <= max_distance and 0 <= y2 <= max_distance:
                return t, x * 4000000 + y2
    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    a1 = 26
    a2 = 56000011
    validate_solution(solve(s, True), (a1, a2))


if __name__ == '__main__':
    main()



