import itertools as it

from utils import *


def solve(d):
    t = 0
    t2 = 0

    nums = ints(d)
    found_i = None
    for i in range(len(nums)):
        for combs in it.combinations(nums, i):
            if sum(combs) == 150:
                t += 1
                if found_i is None:
                    found_i = i
                if found_i == i:
                    t2 += 1

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
