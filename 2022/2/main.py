from utils import *


def solve(d):
    t = 0
    t2 = 0

    ll = lines(d)
    for l in ll:
        op, alt = ord(l[0]) - 65, ord(l[2]) - 88  # Rock, Paper, Scissors, Loose, Draw, Win
        if op == alt:
            t += 3 + alt + 1
        else:
            t += 6 * ((op - alt) % 3 - 1) + alt + 1  # The part in brackets just figures out if we win 1 or loose 0
        if alt == 0:
            t2 += (op - 1) % 3 + 1
        elif alt == 1:
            t2 += op + 4
        else:
            t2 += (op + 1) % 3 + 7

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """A Y
B X
C Z"""
    a1 = 15
    a2 = 12
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



