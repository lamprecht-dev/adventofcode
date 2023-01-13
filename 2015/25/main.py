from utils import *


def solve(d):
    nums = ints(d)
    index = 1
    for i in range(2, nums[1] + 1):
        index += i
    for i in range(nums[1], sum(nums) - 1):
        index += i

    t = 20151125
    for _ in range(1, index):
        t *= 252533
        t = t % 33554393

    return t


def main():
    solution = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    print(solution)


if __name__ == '__main__':
    main()
