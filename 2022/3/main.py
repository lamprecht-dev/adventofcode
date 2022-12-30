from utils import *


def solve(d):
    t = 0
    t2 = 0

    rucksacks = lines(d)
    group = set()
    i = 0
    for r in rucksacks:
        # part 1
        left, right = r[:len(r)//2], r[len(r)//2:]
        for lc in left:
            if lc in right:
                val = ord(lc) - 96
                if val < 1:
                    val += 58
                t += val
                break
        # Part 2
        if i == 0:
            for c in r:
                group.add(c)
        elif i == 1:
            ng = set()
            for g in group:
                if g in r:
                    ng.add(g)
            group = ng
        else:
            for g in group:
                if g in r:
                    val = ord(g) - 96
                    if val < 1:
                        val += 58
                    t2 += val
                    break
            group = set()

        i = (i + 1) % 3

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    a1 = 157
    a2 = 70
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



