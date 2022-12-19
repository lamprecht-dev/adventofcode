import collections as coll
import copy
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq

from utils import *


def time_until_build(target, costs, robots, resources):
    ore = 0
    clay = 0
    obsidian = 0
    if target == "o":
        if robots['o'] == 0:
            return -1
        ore = math.ceil((costs["o"] - resources["o"]) / robots['o'])
    if target == "c":
        if robots['o'] == 0:
            return -1
        ore = math.ceil((costs["c"] - resources["o"]) / robots['o'])
    if target == "ob":
        if robots['o'] == 0 or robots['c'] == 0:
            return -1
        ore = math.ceil((costs["ob_o"] - resources["o"]) / robots['o'])
        clay = math.ceil((costs["ob_c"] - resources["c"]) / robots['c'])
    if target == "g":
        if robots['o'] == 0 or robots['ob'] == 0:
            return -1
        ore = math.ceil((costs["g_o"] - resources["o"]) / robots['o'])
        obsidian = math.ceil((costs["g_ob"] - resources["ob"]) / robots['ob'])

    return max(ore, obsidian, clay) + 1


def collect_in_time(time, robots, resources):
    return {"o": robots["o"] * time + resources['o'], "ob": robots['ob'] * time + resources['ob'],
            "c": robots['c'] * time + resources['c'], "g": robots['g'] * time + resources['g']}


def use_resources(target, costs, resources):
    c = 0
    ob = 0

    if target == "o":
        o = costs["o"]
    elif target == "c":
        o = costs['c']
    elif target == "ob":
        o = costs['ob_o']
        c = costs['ob_c']
    else:
        o = costs['g_o']
        ob = costs['g_ob']

    return {'o': resources['o'] - o, "c": resources['c'] - c, "ob": resources['ob'] - ob, "g": resources['g']}


def to_index(resources, robots, time):
    index = [resources['o'], resources['c'], resources['ob'], resources['g'],
             robots['o'], robots['c'], robots['ob'], robots['g'], time]
    return index


# TODO: Theoretically we could build two robots at a time?
# TODO: ALSO VERY SLOW. Dynamic Programming?
# TODO: Other optimizations?
def most_geodes(costs, robots, time, resources, DP):
    options = ["o", "ob", "c", "g"]
    for dp in DP:
        if dp[0] == to_index(resources, robots, time):
            return dp[1], DP

    if time <= 1:
        geodes = collect_in_time(time, robots, resources)['g']
        dp = (to_index(resources, robots, time), geodes)
        DP.append(dp)
        return geodes, DP

    most = 0
    for o in options:
        t = time_until_build(o, costs, robots, resources)
        if t == -1 or t > time:
            continue
        new_resource = collect_in_time(t, robots, resources)
        new_resource = use_resources(o, costs, new_resource)
        new_robots = copy.deepcopy(robots)
        new_robots[o] += 1
        m, DP = most_geodes(costs, new_robots, time - t, new_resource, DP)
        most = max(most, m)

    dp = (to_index(resources, robots, time), most)
    DP.append(dp)
    return most, DP


def solve(d):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 0

    ll = lines(d)
    i = 1

    for l in ll:
        a, b, c, d, e, f = [int(i) for i in l.split() if i.isdigit()]
        costs = {"o": a, "c": b, "ob_o": c, "ob_c": d, "g_o": e, "g_ob": f}
        result = most_geodes(costs, {"o": 1, "ob": 0, "c": 0, "g": 0}, 24, {"o": 0, "ob": 0, "c": 0, "g": 0}, [])

        t += i * result
        i += 1

    return t, t2


def main():
    test()
    return
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
    a1 = 33
    a2 = 0
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



