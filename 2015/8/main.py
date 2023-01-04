from utils import *


def solve(d):
    t = 0
    t2 = 0

    for line in lines(d):
        decoded_string = bytes(line, "utf-8").decode("unicode_escape")
        escaped = line.translate(str.maketrans({"\\": r"\\", "\"": r"\""}))

        t += len(line) - len(decoded_string) + 2
        t2 += len(escaped) - len(line) + 2

    return t, t2


def main():
    solutions = solve(inp())
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
