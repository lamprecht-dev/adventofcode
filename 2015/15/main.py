from utils import *


def best_score(config, restriction=False):
    if sum(config) == 100:
        cal = 0
        sums = [0] * 4
        for ingI in range(4):
            for ci in range(len(config)):
                cal += config[ci] * cals[ci]
                sums[ingI] += config[ci] * ing[ci][ingI]
            sums[ingI] = max(sums[ingI], 0)
        if restriction and cal != 2000:  # We are doing this technically 4 times so lets just say 2000 instead of 500
            return 0, config
        return math.prod(sums), config

    if len(config) + 1 == len(ing):
        next_config = list(config) + [100 - sum(config)]
        return best_score(next_config, restriction)

    best = 0
    best_config = None
    for i in range(1, 101 - sum(config) - len(ing) + len(config) + 1):
        next_config = list(config) + [i]
        b, bc = best_score(next_config, restriction)
        if b > best:
            best = b
            best_config = bc

    return best, best_config


ing = []
cals = []


def solve(d):
    global ing, cals
    cals = []
    ing = []
    ww = words(d)
    for line in ww:
        ing.append((int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1])))
        cals.append(int(line[10]))

    t = best_score(tuple())
    t2 = best_score(tuple(), True)

    return t[0], t2[0]


def main():
    if test():
        solutions = solve(inp())
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    s = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
    a1 = 62842880
    a2 = 57600000
    return validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
