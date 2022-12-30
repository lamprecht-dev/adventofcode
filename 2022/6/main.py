from utils import *


def substring_of_unique_chars(data, length):
    recent_substring = []
    for c in data:
        recent_substring.append(c)
        if len(recent_substring) > length:
            recent_substring.pop(0)
        if len(recent_substring) < length:
            continue

        if len(set(recent_substring)) == len(recent_substring):
            return "".join(recent_substring)
    return None


def solve(d):
    substring = substring_of_unique_chars(d, 4)
    t = d.index(substring) + 4
    substring = substring_of_unique_chars(d, 14)
    t2 = d.index(substring) + 14

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



