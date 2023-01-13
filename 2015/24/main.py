import collections as coll
import datetime as dt
import functools
import itertools
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


def find_next_group(picked):
    if sum(picked) > target_weight * 2:
        return False

    if sum(picked) == target_weight * 2:
        return True

    for n in nums:
        if n not in picked:
            n_picked = list(picked)
            n_picked.append(n)
            if find_next_group(tuple(n_picked)):
                return True

    return False


def find_sub_groups(picked, picked2=None):
    if picked2 is None:
        picked2 = ()

    if sum(picked) > target_weight2 * 2:
        return False

    if sum(picked) == target_weight2 * 2:  # NEXT STEP!
        if sum(picked2) > target_weight2:
            return False

        if sum(picked2) == target_weight2:  # We found all groups!
            return True

        for n in nums:
            if n not in picked and n not in picked2:
                n_picked = list(picked2)
                n_picked.append(n)
                if find_sub_groups(picked, tuple(n_picked)):
                    return True
        return False

    for n in nums:
        if n not in picked and n not in picked2:
            n_picked = list(picked)
            n_picked.append(n)
            if find_sub_groups(tuple(n_picked), picked2):
                return True
    return False


nums = []
target_weight = math.inf
target_weight2 = math.inf


def solve(d):
    global nums, target_weight, target_weight2

    nums = ints(d)
    target_weight = sum(nums) // 3
    target_weight2 = sum(nums) // 4
    valid_configs = []
    valid_configs2 = []
    stop_looking_for2 = False

    for i in range(1, len(nums)):
        for g1 in it.combinations(nums, i):
            if sum(g1) == target_weight and find_next_group(g1):
                valid_configs.append(g1)
            if sum(g1) == target_weight2 and not stop_looking_for2 and find_sub_groups(g1):
                valid_configs2.append(g1)

        if len(valid_configs) != 0:
            break
        if len(valid_configs2) != 0:
            stop_looking_for2 = True


    t = math.inf
    for vc in valid_configs:
        t = min(t, math.prod(vc))
    t2 = math.inf
    for vc in valid_configs2:
        t2 = min(t2, math.prod(vc))

    return t, t2


def main():
    solutions = solve("""1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113
""")
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
