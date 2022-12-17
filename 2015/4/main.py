import hashlib

from utils import *


def solve(d):
    t = 0

    while True:
        i = d + str(t)
        h = hashlib.md5(i.encode())
        if h.hexdigest()[0:5] == "00000":
            break
        t += 1

    t2 = t
    while True:
        i = d + str(t2)
        h = hashlib.md5(i.encode())
        if h.hexdigest()[0:6] == "000000":
            break
        t2 += 1

    return t, t2


def main():
    # Times: 8:51.92 / 12:32.85
    test()
    solutions = solve(inp())
    print("\n\nSolutions")
    for s in solutions:
        print(s)


def test():
    s = """abcdef"""
    a1 = 609043
    a2 = 6742839
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
