from utils import *

def solve(d):
    t = 0
    t2 = 0

    ll = lines(d)
    for i in range(len(ll)):
        x1, y1, z1 = ints(ll[i].split(","))
        count = 6
        for i2 in range(len(ll)):
            x2, y2, z2 = ints(ll[i2].split(","))
            diff = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
            if diff == 1:
                count -= 1
        t += count

    min_c = None
    max_c = None
    lava = []

    for i in range(len(ll)):
        x, y, z = ints(ll[i].split(","))
        lava.append((x, y, z))
        if min_c is None:
            min_c = (x, y, z)
        else:
            min_c = (min(min_c[0], x), min(min_c[1], y), min(min_c[2], z))
        if max_c is None:
            max_c = (x, y, z)
        else:
            max_c = (max(max_c[0], x), max(max_c[1], y), max(max_c[2], z))

    min_c = (min_c[0] - 1, min_c[1] - 1, min_c[2] - 1)
    max_c = (max_c[0] + 1, max_c[1] + 1, max_c[2] + 1)

    next = [min_c]
    searched = []
    dir = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    while len(next) > 0:
        c = next.pop(0)
        searched.append(c)

        for d in dir:
            n = (c[0] + d[0], c[1] + d[1], c[2] + d[2])

            if n in searched or n in next or n[0] > max_c[0] or \
                    n[1] > max_c[1] or n[2] > max_c[2] or n[0] < min_c[0] or n[1] < min_c[1] or n[2] < min_c[2]:
                continue

            if n in lava:
                t2 += 1
            else:
                next.append(n)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
    a1 = 64
    a2 = 58
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



