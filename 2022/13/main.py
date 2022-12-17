import ast
import copy
import functools

from utils import *


def eval_pairs(l, r):
    l = copy.deepcopy(l)
    r = copy.deepcopy(r)
    i = 0
    while True:
        if len(l) <= i:
            if len(r) <= i:
                return 0
            return -1

        if len(r) <= i:
            return 1

        if type(l[i]) is list and type(r[i]) is not list:
            return eval_pairs(l[i], [r[i]])
        if type(l[i]) is not list and type(r[i]) is list:
            return eval_pairs([l[i]], r[i])

        if type(l[i]) is int:
            if l[i] < r[i]:
                return -1
            elif l[i] > r[i]:
                return 1
        else:
            res = eval_pairs(l[i], r[i])
            if res != 0:
                return res
        i += 1



def solve(d):
    t = 0
    t2 = 1

    pairs = d.split('\n\n')
    i = 1
    packages = [[[2]], [[6]]]

    for pair in pairs:
        l = ast.literal_eval(pair.split('\n')[0])
        r = ast.literal_eval(pair.split('\n')[1])
        packages.append(l)
        packages.append(r)

        if eval_pairs(l, r) == -1:
            t += i

        i += 1

    packages.sort(key=functools.cmp_to_key(eval_pairs))

    for i in range(len(packages)):
        if packages[i] == [[2]] or packages[i] == [[6]]:
            t2 *= i + 1

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    a1 = 13
    a2 = 140
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



