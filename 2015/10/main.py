from utils import *

def solve(d):
    t = 0
    current = d
    for _ in range(50):
        if _ == 40:
            t = len(current)
        prev_dig = None
        dig_count = 1
        out = ""
        for c in current:
            if c == prev_dig:
                dig_count += 1
            else:
                if prev_dig is not None:
                    out += str(dig_count) + prev_dig
                prev_dig = c
                dig_count = 1
        if prev_dig is not None:
            out += str(dig_count) + prev_dig
        current = out

    return t, len(current)


def main():
    solutions = solve(inp())
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



