from utils import *


def solve(d):
    t = ""
    t2 = ""

    line = lines(d)
    d = 5
    pos = (-2, 0)
    pos_l = {(0, -2): "1", (-1, -1): "2", (0, -1): "3", (1, -1): "4", (-2, 0): "5", (-1, 0): "6", (0, 0): "7", (1, 0): "8", (2,  0): "9", (-1, 1): "A", (0, 1): "B", (1, 1): "C", (0, 2): "D"}
    for l in line:
        ins = list(l)
        for i in ins:
            if i == 'U' and d > 3:
                d -= 3
            elif i == 'D' and d < 7:
                d += 3
            elif i == 'L' and d % 3 != 1:
                d -= 1 
            elif i == 'R' and d % 3 != 0:
                d += 1
            mv = dirs[i.lower()]
            np = pos[0] + mv[0], pos[1] + mv[1]
            if abs(np[0]) + abs(np[1]) > 2:
                continue
            pos = np
    
        t += str(d)
        t2 += pos_l[pos]

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
    s = """ULL
RRDDD
LURDL
UUUUD"""
    a1 = "1985"
    a2 = "5DB3"
    return validate_solution(solve(s), (a1, a2))


main()
