from utils import *


def solve(d):
    t = 0
    t2 = 0

    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    ww = words(d)
    for line in ww:
        sue = {line[2][:-1]: int(line[3][:-1]), line[4][:-1]: int(line[5][:-1]), line[6][:-1]: int(line[7])}

        correct = 0
        correct_2 = 0
        for key, val in sue.items():
            if target[key] == val:
                correct += 1
            if key in ['cats', 'trees']:
                if val > target[key]:
                    correct_2 += 1
            elif key in ['pomeranians', 'goldfish']:
                if val < target[key]:
                    correct_2 += 1
            elif target[key] == val:
                correct_2 += 1

        if correct == 3:
            t = line[1][:-1]
        if correct_2 == 3:
            t2 = line[1][:-1]

    return t, t2


def main():
    solutions = solve(inp())
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
