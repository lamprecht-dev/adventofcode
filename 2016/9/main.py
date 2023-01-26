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


def decode(d):
    pointer = 0
    str = ""
    while pointer < len(d):
        if d[pointer] == '(':
            end = pointer + d[pointer:].index(')')
            length, amount = ints(d[pointer + 1:end].split('x'))
            for _ in range(amount):
                str += d[end + 1:end+length + 1]
            pointer = end + length + 1
        else:
            str += d[pointer]
            pointer += 1
    return str


def decode_full(d):
    pointer = 0
    all_compressions = []

    while pointer < len(d):
        if d[pointer] == '(':
            end = pointer + d[pointer:].index(')')

            length, amount = ints(d[pointer + 1:end].split('x'))
            all_compressions.append((pointer, end + 1, length, amount))
            pointer = end + 1
        else:
            pointer += 1

    current_length = len(d)
    while len(all_compressions) > 0:
        comp = all_compressions.pop(0)

        # Change the length
        actual_length = min(comp[2], current_length - comp[1])
        current_length = current_length - comp[1] + comp[0]
        current_length += comp[3] * actual_length

        # edit all comps down the road
        temp_comp = []
        for comp2 in all_compressions:
            if comp2[1] < actual_length + comp[1]:
                # Replicate this multiple times
                for i in range(comp[3]):
                    temp_comp.append((comp2[0] + ((i + 1) * actual_length), comp2[1] + ((i + 1) * actual_length),
                                      comp2[2], comp2[3]))
            else:
                # Just change the index
                temp_comp.append((comp2[0] + comp[3] * actual_length, comp2[1] + comp[3] * actual_length, comp2[2], comp2[3]))

        all_compressions = temp_comp

    return current_length


def solve(d):
    print(decode(d))
    t = len(decode(d))
    t2 = decode_full(d)

    return t, t2


def main():
    # test = "(3x3)XYZ"
    test = "X(8x2)(3x3)ABCY"
    # test = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
    # test = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
    solutions = solve(test)
    # solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

main()
