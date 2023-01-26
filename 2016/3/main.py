import itertools as it
from utils import *


def solve(d):
    t = 0
    t2 = 0

    ll = lines(d)
    for line in ll:
        nums = ints(line)
        any_false = False
        for a,b,c in it.permutations(nums):
            if a + b <= c:
                any_false = True
        if not any_false:
            t += 1
    
    nums = ints(d)
    i = 0
    while True:
        if i + 6 >= len(nums):
            break
        tri = [nums[i], nums[i + 3], nums[i + 6]]
        any_false = False
        for a,b,c in it.permutations(tri):
            if a + b <= c:
                any_false = True
        if not any_false:
            t2 += 1
        if i % 3 == 2:
            i += 6
        i += 1

    return t, t2 


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

main()
