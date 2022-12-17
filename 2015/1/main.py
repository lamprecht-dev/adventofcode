import collections as coll

from utils import *


def solve(d):
    counter = coll.Counter(list(d))
    t = counter['('] - counter[')']
    t2 = 0

    f = 1
    i = 0
    for c in list(d):
        if c == "(":
            f += 1
        else:
            f -= 1

        if f == -1:
            t2 = i
            break
        i += 1

    return t, t2


def main():
    solutions = solve(inp())
    print("Solutions")
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



