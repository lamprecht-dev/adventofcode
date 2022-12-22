import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq
# import sys
# sys.setrecursionlimit(1000000)

from utils import *


class Tile:
    def __init__(self, pos, wall=False):
        self.pos = pos
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.wall = wall

        # For the Cube. Most of the time it stays at None, but certain times we might need to rotate (warping)
        self.left_dir = None
        self.right_dir = None
        self.down_dir = None
        self.up_dir = None

    def neighbors(self, u=None, d=None, l=None, r=None):
        self.left = tuple(l) if l is not None else None
        self.right = tuple(r) if r is not None else None
        self.up = tuple(u) if u is not None else None
        self.down = tuple(d) if d is not None else None
        self.corner = self.is_on_corner()

    def get(self, dir):
        if dir == 0:
            return self.right, self.right_dir
        elif dir == 1:
            return self.down, self.down_dir
        elif dir == 2:
            return self.left, self.left_dir
        else:
            return self.up, self.up_dir

    def is_on_edge(self):
        if self.left is None or self.right is None or self.up is None or self.down is None:
            return True
        return False

    def is_on_corner(self):
        count = 0
        if self.left is None:
            count += 1
        if self.right is None:
            count += 1
        if self.up is None:
            count += 1
        if self.down is None:
            count += 1
        return count == 2

    def link(self, t, dir, dir_change=None):
        if dir == 0:
            self.right = t.pos
            self.right_dir = dir_change
        if dir == 1:
            self.down = t.pos
            self.down_dir = dir_change
        if dir == 2:
            self.left = t.pos
            self.left_dir = dir_change
        if dir == 3:
            self.up = t.pos
            self.up_dir = dir_change

    def find_inward_corner(self, tiles):
        diff_node = [-1, -1]
        count = 0
        edge_dir = []
        if self.is_on_edge():
            return None
        if tiles[self.left].is_on_edge():
            diff_node[1] = self.left[1]
            count += 1
            edge_dir.append(2)
        if tiles[self.right].is_on_edge():
            diff_node[1] = self.right[1]
            count += 1
            edge_dir.append(0)
        if tiles[self.up].is_on_edge():
            diff_node[0] = self.up[0]
            count += 1
            edge_dir.append(3)
        if tiles[self.down].is_on_edge():
            diff_node[0] = self.down[0]
            count += 1
            edge_dir.append(1)

        diff_node = tuple(diff_node)
        if count != 2:  # Not a corner
            return None
        if diff_node in tiles:  # Outward corner
            return None

        return self.pos, edge_dir


def get_tile(pos, tiles):
    if pos not in tiles:
        return None
    return tiles[pos]


def gen_map_tiles(map, part=1):
    tiles = {}
    map_lines = lines(map)
    row_bounds = []
    col_bounds = []
    w = 0
    h = len(map_lines)

    for row in range(len(map_lines)):
        w = max(w, len(map_lines[row]))
        row_bounds.append([math.inf, -math.inf])
        for col in range(len(map_lines[row])):
            if len(col_bounds) <= col:
                col_bounds.append([math.inf, -math.inf])
            m_tile = map_lines[row][col]
            if m_tile == " ":
                continue

            row_bounds[row][0] = min(row_bounds[row][0], col)
            row_bounds[row][1] = max(row_bounds[row][1], col)
            col_bounds[col][0] = min(col_bounds[col][0], row)
            col_bounds[col][1] = max(col_bounds[col][1], row)

            tiles[(row, col)] = Tile((row, col), m_tile == "#")

    for pos, tile in tiles.items():
        u = [sum(x) for x in zip(dirs['u'], pos)]
        d = [sum(x) for x in zip(dirs['d'], pos)]
        l = [sum(x) for x in zip(dirs['l'], pos)]
        r = [sum(x) for x in zip(dirs['r'], pos)]

        # Wrapping
        if part == 1:
            if col_bounds[u[1]][0] > u[0]:
                u[0] = col_bounds[u[1]][1]
            if col_bounds[d[1]][1] < d[0]:
                d[0] = col_bounds[u[1]][0]
            if row_bounds[l[0]][0] > l[1]:
                l[1] = row_bounds[l[0]][1]
            if row_bounds[r[0]][1] < r[1]:
                r[1] = row_bounds[r[0]][0]
        else:
            if col_bounds[u[1]][0] > u[0]:
                u = None
            if col_bounds[d[1]][1] < d[0]:
                d = None
            if row_bounds[l[0]][0] > l[1]:
                l = None
            if row_bounds[r[0]][1] < r[1]:
                r = None

        tiles[pos].neighbors(u, d, l, r)

    if part == 2:
        # Find all the inward corners. And move along them UNTIL you have on two edges a direction change
        # to find the inward corner, we need to find a tile that has all for directions set.
        # Walk into TWO directions and check if they have a side missing
        inward_corners = []
        for pos, tile in tiles.items():
            ic = tile.find_inward_corner(tiles)
            if ic is not None:
                inward_corners.append(ic)

        dir_codec = {0: 'r', 1: 'd', 2: 'l', 3: 'u'}
        for ic in inward_corners:
            d1 = ic[1][0]
            d2 = ic[1][1]
            ddiff = (d1 - d2) % 4 - 2  # what direction 2 initially from 1
            p1 = ic[0]
            p2 = ic[0]

            c1_changed = False
            c2_changed = False

            while True:
                p1 = tuple([sum(x) for x in zip(dirs[dir_codec[d1]], p1)])
                p2 = tuple([sum(x) for x in zip(dirs[dir_codec[d2]], p2)])
                t1 = get_tile(p1, tiles)
                t2 = get_tile(p2, tiles)
                c1 = t1.corner
                c2 = t2.corner

                t1.link(t2, (d1 + ddiff) % 4, d2 - d1)
                t2.link(t1, (d2 - ddiff) % 4, d1 - d2)

                if c1 and c2:
                    break
                if c1 and not c1_changed:
                    d1 -= ddiff
                    d1 %= 4
                    p1 = tuple([sum(x) for x in zip(dirs[dir_codec[(d1 + 2) % 4]], p1)])  # Move one back
                    c1_changed = True
                else:
                    c1_changed = False
                if c2 and not c2_changed:
                    d2 += ddiff
                    d2 %= 4
                    p2 = tuple([sum(x) for x in zip(dirs[dir_codec[(d2 + 2) % 4]], p2)])  # Move one back
                    c2_changed = True
                else:
                    c2_changed = False

    return tiles, (row_bounds, col_bounds), (w, h)


def solve(d, part=1):
    map, code = d.split("\n\n")
    code = re.split('(\d+)', code)[1:-1]
    tiles, bounds, dimension = gen_map_tiles(map, part)
    pos = (0, int(bounds[0][0][0]))
    dir = 0

    for c in code:
        if c == "L":
            dir -= 1
            if dir < 0:
                dir += 4
        elif c == "R":
            dir += 1
            if dir > 3:
                dir -= 4
        else:
            for _ in range(int(c)):
                n, d_change = tiles[pos].get(dir)
                # print(pos, dir, n)
                if tiles[n].wall:
                    break
                pos = n
                if d_change is not None:
                    dir = (dir + d_change) % 4

    t = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir

    return t


def main():
    test()
    solutions = (solve(inp()), solve(inp(), 2))
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
    a1 = 6032
    a2 = 5031
    validate_solution((solve(s), solve(s, 2)), (a1, a2))


if __name__ == '__main__':
    main()



