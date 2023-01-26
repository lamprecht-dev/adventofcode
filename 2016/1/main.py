from utils import *


def solve(d):
    t = 0
    t2 = 0

    ww = words(d)[0]
    dir = 0
    x, y = 0, 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    locs = set()
    for w in ww:
        ins = w.rstrip(",")
        if ins[0:1] == "R":
            dir += 1
        else:
            dir -= 1
        dir = dir % 4
        for _ in range(int(ins[1:])):
            x += dirs[dir][0]
            y += dirs[dir][1]
            if (x, y) in locs and t2 == 0:
                t2 = abs(x) + abs(y)
            locs.add((x, y))
  
    t = abs(x) + abs(y)

    return t, t2


def main():
    solutions = solve(inp())
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

main()
