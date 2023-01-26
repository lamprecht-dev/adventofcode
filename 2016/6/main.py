import collections as coll

from utils import *


def solve(d):
    t = ''
    t2 = ''

    ll = lines(d)

    counters = []
    for i in range(len(ll[0])):
        counters.append(coll.Counter())

    for line in ll:
        for i in range(len(line)):
            counters[i].update(line[i])

    for c in counters:
        t += c.most_common(1)[0][0]
        t2 += c.most_common()[-1][0]

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
    s = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
    a1 = 'easter'
    a2 = 'advent'
    return validate_solution(solve(s), (a1, a2))


main()
