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


def solve(d, is_test=False):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    blocked = set()
    signals = []
    beacons = set()
    possible_locations = set()
    max_range = 20 if is_test else 4000000

    # for i in range(max_range + 1):
    #     possible_locations.add((i, 0))
    #     possible_locations.add((i, max_range))
    #     possible_locations.add((0, i))
    #     possible_locations.add((max_range, i))

    for ll in lines(d):
        ll = ll.replace('Sensor at ', '').replace('x=', '').replace(' y=', '').split(': closest beacon is at ')
        signal = None
        for i in ll:
            nums = ints(i, ",")
            if signal is None:
                signal = nums
            else:
                beacons.add(tuple(nums))
                diff = nums[0] - signal[0], nums[1] - signal[1]
                dist = abs(diff[0]) + abs(diff[1])
                signals.append((signal, dist))

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

                # print(signal, nums, dist)

                for i in range(dist * 2 + 3):
                    ii = i - dist - 1
                    block_amount = abs(abs(ii) - dist - 1)
                    possible_locations.add((signal[0] + ii, signal[1] + block_amount))
                    possible_locations.add((signal[0] + ii, signal[1] - block_amount))

                signal = None

    print(len(possible_locations))

    for b in beacons:
        if b in possible_locations:
            possible_locations.remove(b)
        if b in blocked:
            blocked.remove(b)

    t = len(blocked)

    possible = list(possible_locations)

    for p in possible:
        if (p[0] < 0 or p[0] > max_range or p[1] < 0 or p[1] > max_range) and p in possible_locations:
            possible_locations.remove(p)
            continue
        for s in signals:
            loc, dist = s
            diff = abs(loc[0] - p[0]) + abs(loc[1] - p[1])

            if diff <= dist:
                possible_locations.remove(p)
                break

    print(len(possible_locations))
    print(possible_locations)

    distress = list(possible_locations)[0]
    t2 = distress[0] * 4000000 + distress[1]

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



