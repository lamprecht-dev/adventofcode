import collections as coll
import datetime as dt
import functools
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
    for n in valve[1]:
        neighbors.append(valves[n])

    return neighbors


def sum_valves(d):
    return sum([x for (_, x, _) in d])


@functools.lru_cache(maxsize=None)
def highest_release(cur, opened, lim, pleft=0, dcur=None, dlim=None):
    global V, Paths

    if dcur is None:
        dcur = cur
    if dlim is None:
        dlim = lim

    new_opened = tuple(sorted(opened + (cur, )))  # Sorted
    # new_opened = tuple(list(opened) + [cur])  # Not Sorted

    my_release = V[cur][0] * lim
    if lim <= 1:  # Not enough time to go anywhere and open something (which takes 2 minutes)
        if pleft > 0:  # If we still have the elephant let him do the rest in his full time
            return highest_release(dcur, new_opened, dlim, pleft - 1)
        return [(cur, 0, lim)]

    max_val = []
    for v in V:
        if v[0] == 0:  # No flow rate, just skip
            continue

        vi = V.index(v)
        if vi in opened or vi == cur:  # It's already opened or its self
            continue

        walk = Paths[cur][vi] + 1  # 1min to open the valve
        val = highest_release(vi, new_opened, lim - walk, pleft, dcur, dlim)
        val_sum = sum_valves(val)
        max_val_sum = sum_valves(max_val)
        if val_sum > max_val_sum:
            max_val = val

    # Instead of just one person doing everything,
    # I could also check what if I had stopped here and the elephant did the rest of the valves?
    if pleft > 0:
        val = highest_release(dcur, new_opened, dlim, pleft - 1)
        val_sum = sum_valves(val)
        max_val_sum = sum_valves(max_val)
        if val_sum > max_val_sum:
            max_val = val

    return max_val + [(cur, my_release, lim)]


# target, current, V
def shortest_walk(t, c, V):
    if t is c:
        return 0
    queue = coll.deque()
    visited = set()

    nn = get_neighbors(c, V)
    for n in nn:
        queue.append((V.index(n), 1))

    while len(queue) > 0:
        q = queue.popleft()
        if q[0] == V.index(t):
            return q[1]

        nn = get_neighbors(V[q[0]], V)
        for n in nn:
            if V.index(n) in visited:
                continue

            already_in_queue = False
            for q2 in queue:
                if q2[0] == V.index(n):
                    already_in_queue = True
                    break
            if already_in_queue:
                continue

            queue.append((V.index(n), q[1] + 1))

        visited.add(q[0])

    return 0


def generate_lookup(V):
    paths = {}

    for v1 in V:
        if Valve_Index[V.index(v1)] != "AA" and v1[0] == 0:
            continue
        ts = {}
        for v2 in V:
            if Valve_Index[V.index(v2)] != "AA" and v2[0] == 0:
                continue
            ts[V.index(v2)] = shortest_walk(v2, v1, V)
        paths[V.index(v1)] = ts

    return paths


V = []
Valve_Index = []
Paths = {}


def solve(d):
    global Paths, Valve_Index, V
    ll = lines(d)
    V = []
    Valve_Index = []

    for l in ll:
        ww = l.split(';')
        leads = ww[1].strip('tunnels lead to ').strip('tunnel leads to ').strip("valves ").strip("valve ").split(", ")
        valve = ww[0].split()[1], int(ww[0].split()[4].strip("rate=")), leads
        Valve_Index.append(valve[0])
        V.append(valve)

    for v in V:
        no = []
        i = Valve_Index.index(v[0])
        for o in v[2]:
            no.append(Valve_Index.index(o))
        v = v[1], no
        V[i] = v

    Paths = generate_lookup(V)
    print(Paths)

    highest_release.cache_clear()
    t = highest_release(Valve_Index.index('AA'), (), 30)
    t2 = highest_release(Valve_Index.index('AA'), (), 26, 1)

    print(sum_valves(t2), t2)
    return sum_valves(t), sum_valves(t2)


def main():
    test()
    solutions = solve(inp())    # 1488
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



