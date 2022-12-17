from utils import *


def is_nice1(l):
    vowels = 0
    for s in l:
        if s in "aeiou":
            vowels += 1
    repeat = False
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            repeat = True
    bad_string = "ab" in l or "cd" in l or "pq" in l or "xy" in l
    return vowels >= 3 and repeat and not bad_string


def is_nice2(l):
    repeat = False
    for i in range(len(l) - 1):
        for j in range(i + 2, len(l) - 1):
            if l[i:i + 2] == l[j:j + 2]:
                repeat = True
    repeat2 = False
    for i in range(len(l) - 2):
        if l[i] == l[i + 2]:
            repeat2 = True
    return repeat and repeat2


def solve(d):
    t = 0
    t2 = 0

    ll = lines(d)
    for l in ll:
        if is_nice1(l):
            t += 1
        if is_nice2(l):
            t2 += 1

    return t, t2


def main():
    # Times: 16:26.02 / 22:26.89 BUT EDITED FILE SINCE
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb"""
    a1 = 2
    a2 = 0
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



