from utils import *


def solve(d):
    t = 0
    t2 = """"""

    x = 1
    c = 0  # cycle
    i = 0  #instruction
    end_of_cycle = False

    ww = words(d)
    computing = False

    while not end_of_cycle:
        # Part 2 - Needs to actually happen before c gets incremented
        cr = c % 40
        if x - 1 == cr or x == cr or x + 1 == cr:
            t2 += "#"
        else:
            t2 += "."
        if cr == 39:
            t2 += "\n"

        # Part 1
        c += 1
        if c in [20, 60, 100, 140, 180, 220]:
            t += c * x

        if len(ww) > i:
            if ww[i][0] == "noop":
                i += 1
            elif ww[i][0] == "addx" and not computing:
                computing = True
            elif ww[i][0] == "addx":
                x += int(ww[i][1])
                computing = False
                i += 1

        if len(ww) <= i:
            end_of_cycle = True

    return (t, t2)


if __name__ == '__main__':
    s = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    a1 = 13140
    a2 = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

    validate_solution(solve(s), (a1, a2))
    soutions = solve(inp())
    print("\n\nSolutions")
    for s in soutions:
        print(s)

