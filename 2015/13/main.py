import collections as coll
import itertools as it

from utils import *


prefs = coll.defaultdict(lambda: coll.defaultdict(lambda: 0))
names = []


def best_score(amnt):
    best = 0
    for perms in it.permutations(range(amnt), amnt):
        if perms[0] != 0:
            continue

        sum_all = prefs[perms[0]][perms[-1]] + prefs[perms[-1]][perms[0]]
        for i in range(len(perms) - 1):
            sum_all += prefs[perms[i]][perms[i + 1]] + prefs[perms[i + 1]][perms[i]]
        best = max(best, sum_all)
    return best


def solve(d):
    global names, prefs
    ww = words(d)
    for line in ww:
        name1 = line[0]
        name2 = line[10][:-1]
        if name1 not in names:
            names.append(name1)
        if name2 not in names:
            names.append(name2)

        mod = 1 if line[2] == "gain" else -1

        prefs[names.index(name1)][names.index(name2)] = int(line[3]) * mod

    t = best_score(len(names))
    t2 = best_score(len(names) + 1)

    return t, t2


def main():
    if test():
        solutions = solve(inp())
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    s = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
    a1 = 330
    a2 = None
    return validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
