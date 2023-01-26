from utils import *


def solve(d):
    W, H = 50, 6
    S = set()  # X, Y

    ww = words(d)
    for line in ww:
        if line[0] == 'rect':
            a,b = ints(line[1].split('x'))
            for ai in range(a):
                for bi in range(b):
                    S.add((ai, bi))
        elif line[1] == 'column':
            x = int(line[2].split('=')[1])
            amnt = int(line[4])
            NS = set()
            for s in S:
                if s[0] == x:
                    NS.add((x, (s[1] + amnt) % H))
                else:
                    NS.add(s)
            S = NS
        else:
            y = int(line[2].split('=')[1])
            amnt = int(line[4])
            NS = set()
            for s in S:
                if s[1] == y:
                    NS.add(((s[0] + amnt) % W, y))
                else:
                    NS.add(s)
            S = NS

    disp = ""
    for y in range(H):
        row = ""
        for x in range(W):
            row += "#" if (x, y) in S else " "
        disp += row + "\n"

    return len(S), disp


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

main()
