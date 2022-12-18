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


def find_best_path(c, his, V, P, DP, lim, players_left=0, default_c=None, default_lim=None):
    if default_c is None:
        default_c = c
    if default_lim is None:
        default_lim = lim
    best_value = 0

    hk = his_to_key(his)
    if hk not in DP[players_left]:
        DP[players_left][hk] = {}
    if c[0] not in DP[players_left][hk]:
        DP[players_left][hk][c[0]] = {}
    if lim in DP[players_left][hk][c[0]]:
        return DP[players_left][hk][c[0]][lim], DP
    else:
        DP[players_left][hk][c[0]][lim] = 0

    if lim <= 1:
        return 0, DP

    for vv in V:
        v = V[vv]

        if v is c or v in his or v[1] == 0:
            continue

        walk = P[c[0]][v[0]]

        val, DP = find_best_path(v, his + [c], V, P, DP, lim - walk - 1, players_left, default_c, default_lim)
        best_value = max(best_value, val)

    if players_left > 0:
        val, DP = find_best_path(default_c, his + [c], V, P, DP, default_lim)
        best_value = max(val, best_value)

    my_val = c[1] * lim

    DP[players_left][hk][c[0]][lim] = best_value + my_val

    return best_value + my_val, DP


def his_to_key(his):
    key = set()
    for h in his:
        key.add(h[0])
    key = sorted(list(key))
    key = "".join(key)

    return key

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


def generate_lookup(V):
    paths = {}

    for v1 in V:
        ts = {}
        for v2 in V:
            ts[v2] = shortest_walk(V[v2], V[v1], V)
        paths[v1] = ts

    return paths


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

    paths = generate_lookup(V)

    t = find_best_path(V['AA'], [], V, paths, {1: {}, 0: {}}, 30)[0]
    t2 = find_best_path(V['AA'], [], V, paths, {1: {}, 0: {}}, 26, 1)[0]

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
    a2 = 1707  # 898 + 809
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



