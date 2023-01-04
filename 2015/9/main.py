import collections as coll
import functools
import itertools as it

from utils import *


@functools.lru_cache(maxsize=None)
def shortest_path(cur, tar, his, check_longest=False):
    if cur == tar:
        return 0

    shortest = math.inf
    longest = -math.inf
    for p in paths[cur]:
        if p == tar:
            if len(his) >= len(cities) - 2:
                return paths[cur][p]
        elif p not in his:
            new_his = set(his)
            new_his.add(cur)
            new_his = frozenset(new_his)

            val = shortest_path(p, tar, new_his, check_longest)
            shortest = min(shortest, val + paths[cur][p])
            longest = max(longest, val + paths[cur][p])
    if check_longest:
        return longest
    return shortest


paths = coll.defaultdict(dict)
cities = []


def solve(d):
    global paths, cities
    shortest_path.cache_clear()
    paths = coll.defaultdict(dict)
    cities = []

    ww = words(d)
    for line in ww:
        if line[0] not in cities:
            cities.append(line[0])
        if line[2] not in cities:
            cities.append(line[2])

        paths[cities.index(line[0])][cities.index(line[2])] = int(line[4])
        paths[cities.index(line[2])][cities.index(line[0])] = int(line[4])

    t = math.inf
    t2 = -math.inf
    for a, b in it.combinations(range(len(cities)), 2):
        t = min(t, shortest_path(a, b, frozenset({})))
        t2 = max(t2, shortest_path(a, b, frozenset({}), True))

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
    s = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    a1 = 605
    a2 = 982
    return validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
