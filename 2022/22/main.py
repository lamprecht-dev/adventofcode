import re

from utils import *


# The heart of the problem. A well defined Tile class to make traversing easier
class Tile:
    def __init__(self, pos, wall=False):
        self.pos = pos
        self.wall = wall
        # Those are the next notes. We simply get them ones defined and use the information to find next tile
        # We deal with warping in the gen_map_tiles function
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        # For the Cube. Most of the time it stays at None, but certain times we might need to rotate (warping)
        self.left_dir = None
        self.right_dir = None
        self.down_dir = None
        self.up_dir = None
        self.corner = False

    # A quick way to initially set the neighbors.
    def neighbors(self, u=None, d=None, l=None, r=None):
        self.left = tuple(l) if l is not None else None
        self.right = tuple(r) if r is not None else None
        self.up = tuple(u) if u is not None else None
        self.down = tuple(d) if d is not None else None
        self.corner = self.is_on_corner()

    # Simple function to return tile of dir
    def get(self, dir):
        if dir == 0:
            return self.right, self.right_dir
        elif dir == 1:
            return self.down, self.down_dir
        elif dir == 2:
            return self.left, self.left_dir
        else:
            return self.up, self.up_dir

    # Helper function to get if its on an edge
    # At least one side needs to be none
    def is_on_edge(self):
        if self.left is None or self.right is None or self.up is None or self.down is None:
            return True
        return False

    # Same as is on edge, except exactly two need to be none
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

    # To link to neighbors after we initially set neighbors above.
    #   This is to dynamically set the right neighbor depending on the dir for the 3D Cube
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

    # The function for Part 2 to find the inward corners
    def find_inward_corner(self, tiles):
        diff_node = [-1, -1]
        count = 0
        edge_dir = []
        # If this is on the edge we don't want it
        if self.is_on_edge():
            return None
        # Now we find each of the neighbors that ARE on the edge.
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

        # If those are exactly two neighbors we are on a corner.
        # To find if its inward or outward, we simply check if the diff note,
        #  the note that is adjacent to both directions exists or not
        diff_node = tuple(diff_node)
        if count != 2:  # Not a corner
            return None
        if diff_node in tiles:  # Outward corner
            return None

        return self.pos, edge_dir


# Helper function
def get_tile(pos, tiles):
    # Python seems to freak out sometimes if I get tiles from a mixed tuple even though it is an int tuple.
    #  So here is a function to help python calm down
    if pos not in tiles:
        return None
    return tiles[pos]


# Setup the Map
def gen_map_tiles(map, part=1):
    tiles = {}
    map_lines = lines(map)
    row_bounds = []
    col_bounds = []
    w = 0
    h = len(map_lines)

    # Step 1: Generate each tile as wall or walkway and save in tiles lookup/hash map
    for row in range(len(map_lines)):
        w = max(w, len(map_lines[row]))
        row_bounds.append([math.inf, -math.inf])
        for col in range(len(map_lines[row])):
            if len(col_bounds) <= col:
                col_bounds.append([math.inf, -math.inf])
            m_tile = map_lines[row][col]
            if m_tile == " ":  # These are not part of the map so need to be ignored
                continue

            # We also do a thing that helps us later to determine min and max locations of each row and col
            row_bounds[row][0] = min(row_bounds[row][0], col)
            row_bounds[row][1] = max(row_bounds[row][1], col)
            col_bounds[col][0] = min(col_bounds[col][0], row)
            col_bounds[col][1] = max(col_bounds[col][1], row)

            tiles[(row, col)] = Tile((row, col), m_tile == "#")

    # Step 2: Go through each tile and define it's neighbors
    for pos, tile in tiles.items():
        # Most of them are simple. Just use the neighboring positions, find them and get their tile note
        u = [sum(x) for x in zip(dirs['u'], pos)]
        d = [sum(x) for x in zip(dirs['d'], pos)]
        l = [sum(x) for x in zip(dirs['l'], pos)]
        r = [sum(x) for x in zip(dirs['r'], pos)]

        # Wrapping
        # This is simple in step 1. Simple use the col and row min max that we found earlier to determine which values
        #  need to be replaced with the ones on the opposite site of the map
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
            # In part 2 it get's way more complicated as we now need to think of it as a 3d cube
            #  So for now just set them as None
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
        # Find all the inward corners. And move along them UNTIL you have on BOTH edges a direction change (a corner)
        #  To find the inward corner, we need to find a tile that has all for directions set.
        #  Walk into TWO directions and check if they have a side missing. That is an corner
        #  What makes the corner inward is that the the oposite tile that both are adjasent to does not exist.
        #  If it does, its an outward corner. Which we don't need
        inward_corners = []
        for pos, tile in tiles.items():
            ic = tile.find_inward_corner(tiles)  # Get all inward corners
            if ic is not None:
                inward_corners.append(ic)

        # Now we want to go through each inward corner and walk along the
        # edges until we have two corners at the same time
        dir_codec = {0: 'r', 1: 'd', 2: 'l', 3: 'u'}
        for ic in inward_corners:
            # This took a lot of tinkering. Which did't make it the fastest way to solve it, but a sound way
            d1 = ic[1][0]   # Directions of the paths we walk on
            d2 = ic[1][1]
            ddiff = (d1 - d2) % 4 - 2  # The difference in directions.
            p1 = ic[0]  # The positions that we start on
            p2 = ic[0]

            # Since a corner has two missing edges, we need to be on it twice. But that can give some trouble so we
            # just keep in mind if we just changed directions or not
            c1_changed = False
            c2_changed = False

            while True:
                # Find next position along path, and get the tile and weather or not the tile was a corner
                p1 = tuple([sum(x) for x in zip(dirs[dir_codec[d1]], p1)])
                p2 = tuple([sum(x) for x in zip(dirs[dir_codec[d2]], p2)])
                t1 = get_tile(p1, tiles)
                t2 = get_tile(p2, tiles)
                c1 = t1.corner
                c2 = t2.corner

                # Now we do a simple link. This is the heart of the problem which needs all the math beforehand
                # ARG1 gives the note we are linking to.
                # ARG2 gives which side we need to link to. E.g when we walk up it can be either left or right,
                #  depending on relative path direction at the beginning to the other path.
                # ARG3 gives the direction change once we wrap around, so the algorithm at the bottom is not affected
                t1.link(t2, (d1 + ddiff) % 4, d2 - d1)
                t2.link(t1, (d2 - ddiff) % 4, d1 - d2)

                # Now we check for corners. If both are corners,
                #  we are finished with this section and go to next inward corner
                # If only one is corner and hasn't changed yet, we change its direction according to ddiff from the
                #  start of the path. Then we move one step back as the alg will need to go do this corner again
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


# Traverse Through the Map
def solve(d, part=1):
    map, code = d.split("\n\n")
    code = re.split('(\d+)', code)[1:-1]                    # Splitting Code into chunks of letters and numbers
    tiles, bounds, dimension = gen_map_tiles(map, part)     # Biggest part of the solve. The proper generation of the map
    pos = (0, int(bounds[0][0][0]))                         # Setting initial conditions
    dir = 0

    # Traversing through the map is trivial once the map has been properly generated
    for c in code:
        # Either change direction
        if c == "L":
            dir = (dir - 1) % 4
        elif c == "R":
            dir = (dir + 1) % 4
        else:
            # Or walk for c steps into direction, until you meet a wall. Since we defined the tile class well
            #  We won't need to do any more extra conditioning
            for _ in range(int(c)):
                n, d_change = tiles[pos].get(dir)
                if tiles[n].wall:
                    break
                pos = n
                # This is added in part two. As wrapping around can change the direction on the flat map, we want to
                #  keep that in our mind as we traverse
                if d_change is not None:
                    dir = (dir + d_change) % 4

    # Get final position and direction and form the answer
    t = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir

    return t


# Setup the Solve
def main():
    test()
    solutions = (solve(inp()), solve(inp(), 2))
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


# Setup the Test to verify results
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
