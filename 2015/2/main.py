import itertools as it

from utils import *


def solve(d):
    t = 0
    t2 = 0

    ww = words(d, "x")
    for line in ww:
        if line[0] == '':
            continue

        sides = sorted([int(line[0]), int(line[1]), int(line[2])])
        perm = it.combinations(sides, 2)
        sub = 0
        smallest = math.inf

        for p in perm:
            sub += 2 * math.prod(p)
            smallest = min(math.prod(p), smallest)

        t += sub + smallest
        it.product(sides)
        t2 += math.prod(sides) + sides[0] * 2 + sides[1] * 2

    return t, t2


def main():
    solutions = solve(inp())
    print("Solutions")
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



