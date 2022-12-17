import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq

from utils import *


def get_neighbors(valve, valves):
    neighbors = []
    for n in valve[2]:
        neighbors.append(valves[n])

    return neighbors


# TODO: Have the solutions one after ANTOTHER, once we reach end,
#  check if player left is 1 and then redo with current his
def find_best_path(c, his, V, lim, players_left=0, default_c=None, default_lim=None):
    if default_c is None:
        default_c = c
    if default_lim is None:
        default_lim = lim
    best_value = 0

    if lim <= 1:
        if players_left > 0:
            return find_best_path(default_c, his, V, default_lim)
        return 0

    for vv in V:
        v = V[vv]

        if v is c or v in his or v[1] == 0:
            continue

        walk = shortest_walk(v, c, V)

        val = find_best_path(v, his + [c], V, lim - walk - 1, players_left, default_c, default_lim)
        best_value = max(best_value, val)

    my_val = c[1] * lim
    return best_value + my_val


# target, current, V
def shortest_walk(t, c, V):
    queue = []
    visited = []

    nn = get_neighbors(c, V)
    for n in nn:
        queue.append((n[0], 1))

    while len(queue) > 0:
        q = queue.pop(0)
        if q[0] == t[0]:
            return q[1]

        nn = get_neighbors(V[q[0]], V)
        for n in nn:
            if n in visited:
                continue

            queue.append((n[0], q[1] + 1))

        visited.append(V[q[0]])

    return 0


def solve(d):
    # stats(d)
    # print("Input: ", repr(d))
    t = 0
    t2 = 0

    V = dict()

    ll = lines(d)
    for l in ll:
        ww = l.split(';')
        leads = ww[1].strip('tunnels lead to ').strip('tunnel leads to ').strip("valves ").strip("valve ").split(", ")
        valve = ww[0].split()[1], int(ww[0].split()[4].strip("rate=")), leads
        V[ww[0].split()[1]] = valve

    t = find_best_path(V['AA'], [], V, 30)
    t2 = find_best_path(V['AA'], [], V, 26, 1)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
    a1 = 1651
    a2 = 1707
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



