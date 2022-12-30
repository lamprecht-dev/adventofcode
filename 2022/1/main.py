from utils import *


def solve(d):
    elves = d.split("\n\n")
    e_sums = []
    for e in elves:
        nums = ints(lines(e))
        e_sums.append(sum(nums))
    e_sums.sort(reverse=True)

    return max(e_sums), sum(e_sums[:3])


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    a1 = 24000
    a2 = 45000
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



