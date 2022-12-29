import functools
# import sys
# sys.setrecursionlimit(1000000000)

from utils import *


def get_inventory(costs, inventory, robots, adjust):
    n_inv = []
    for i in range(len(robots)):
        n_val = inventory[i] + robots[i] + adjust[i]
        # We don't need an overflow of materials. We can just keep deleting the overflow, like lets say 3x the max cost
        if i == ORE:
            max_ore_cost = max(costs[ORE], costs[CLAY], costs[OB_ORE], costs[GEO_ORE]) * 3
            n_val = min(max_ore_cost, n_val)
        if i == CLAY:
            max_ore_cost = costs[OB_CLAY] * 3
            n_val = min(max_ore_cost, n_val)
        if i == OBSIDIAN:
            max_ore_cost = costs[GEO_OB] * 3
            n_val = min(max_ore_cost, n_val)

        n_inv.append(n_val)
    return tuple(n_inv)


@functools.lru_cache(maxsize=None)
def most_geodes(costs, time, inventory=None, robots=None):
    if inventory is None:
        inventory = (0, 0, 0, 0)
    if robots is None:
        robots = (1, 0, 0, 0)

    if time <= 1:
        return inventory[GEODE] + robots[GEODE] * time

    max_geodes = 0
    can_build_geo = False
    if inventory[ORE] >= costs[GEO_ORE] and inventory[OBSIDIAN] >= costs[GEO_OB]:
        n_inv = get_inventory(costs, inventory, robots, (-costs[GEO_ORE], 0, -costs[GEO_OB], 0))
        n_robs = (robots[ORE], robots[CLAY], robots[OBSIDIAN], robots[GEODE] + 1)
        geodes = most_geodes(costs, time - 1, n_inv, n_robs)
        max_geodes = max(max_geodes, geodes)
        can_build_geo = True
    if inventory[ORE] >= costs[ORE] and robots[ORE] < max(costs[ORE], costs[CLAY], costs[OB_ORE], costs[GEO_ORE]) \
            and not can_build_geo:
        n_inv = get_inventory(costs, inventory, robots, (-costs[ORE], 0, 0, 0))
        n_robs = (robots[ORE] + 1, robots[CLAY], robots[OBSIDIAN], robots[GEODE])
        geodes = most_geodes(costs, time - 1, n_inv, n_robs)
        max_geodes = max(max_geodes, geodes)
    if inventory[ORE] >= costs[CLAY] and robots[CLAY] < costs[OB_CLAY] \
            and not can_build_geo:
        n_inv = get_inventory(costs, inventory, robots, (-costs[CLAY], 0, 0, 0))
        n_robs = (robots[ORE], robots[CLAY] + 1, robots[OBSIDIAN], robots[GEODE])
        geodes = most_geodes(costs, time - 1, n_inv, n_robs)
        max_geodes = max(max_geodes, geodes)
    if inventory[ORE] >= costs[OB_ORE] and inventory[CLAY] >= costs[OB_CLAY] and robots[OBSIDIAN] < costs[GEO_OB] \
            and not can_build_geo:
        n_inv = get_inventory(costs, inventory, robots, (-costs[OB_ORE], -costs[OB_CLAY], 0, 0))
        n_robs = (robots[ORE], robots[CLAY], robots[OBSIDIAN] + 1, robots[GEODE])
        geodes = most_geodes(costs, time - 1, n_inv, n_robs)
        max_geodes = max(max_geodes, geodes)

    if not can_build_geo:
        # Just waiting
        n_inv = get_inventory(costs, inventory, robots, (0, 0, 0, 0))
        geodes = most_geodes(costs, time - 1, n_inv, robots)
        max_geodes = max(max_geodes, geodes)

    return max_geodes

# Names for easy indexing
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
OB_ORE = 2  # Cost
OB_CLAY = 3  # Cost
GEO_ORE = 4  # Cost
GEO_OB = 5  # Cost


def solve(d):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 1

    ll = lines(d)
    i = 1
    for l in ll:
        ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian = \
            [int(i) for i in l.split() if i.isdigit()]
        costs = (ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian)
        result = most_geodes(costs, 32)
        print(i, result)
        t2 *= result
        i += 1
        if i >= 4:
            break

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)

def test():
    s = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
    a1 = 33
    a2 = 3472
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



