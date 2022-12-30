from utils import *


def solve(d):
    t = 0
    t2 = 0

    ll = lines(d)
    for line in ll:
        elves = line.replace("\n", "").split(",")
        e1 = elves[0].split("-")
        e2 = elves[1].split("-")

        if (int(e1[0]) >= int(e2[0]) and int(e1[1]) <= int(e2[1])) or \
                (int(e1[0]) <= int(e2[0]) and int(e1[1]) >= int(e2[1])):
            t += 1
        if (int(e2[1]) >= int(e1[0]) >= int(e2[0])) or (int(e2[1]) >= int(e1[1]) >= int(e2[0])) or \
                (int(e1[1]) >= int(e2[0]) >= int(e1[0])) or (int(e1[1]) >= int(e2[1]) >= int(e1[0])) or \
                (int(e1[0]) >= int(e2[0]) and int(e1[1]) <= int(e2[1])) or \
                (int(e1[0]) <= int(e2[0]) and int(e1[1]) >= int(e2[1])):
            t2 += 1

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    a1 = 2
    a2 = 4
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



