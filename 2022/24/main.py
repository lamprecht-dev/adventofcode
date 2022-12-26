import collections as coll

from utils import *

def solve(d):
    t = 0

    dirs = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0), "@": (0, 0)}
    G, h, w = grid(d)
    B = []
    p1 = ()
    p2 = ()

    for row in range(h):
        for col in range(w):
            if G[row][col] != "." and 0 < row < h - 1 and 0 < col < w - 1:
                b = [row, col, dirs[G[row][col]]]
                B.append(b)
            if row == 0 and G[row][col] == ".":
                p1 = (row, col)
            elif row == h - 1 and G[row][col] == ".":
                p2 = (row, col)

    # To simplify future calcs
    h -= 2
    w -= 2

    # Update Blizzards
    def next_B():
        for b in B:
            row, col, (row_d, col_d) = b
            y = row + row_d
            x = col + col_d
            y = ((y - 1) % h) + 1
            x = ((x - 1) % w) + 1
            b[0] = y
            b[1] = x

    def get_B_set():
        Bset = set()
        for b in B:
            by, bx, _ = b
            Bset.add((by, bx))
        return Bset

    BC = get_B_set()
    nxt = coll.deque()
    nxt.append((p1, 0, False, False)) # Coord, Time, Seen End, Seen Start
    max_time = -1
    seen = set()

    # Because of some reason I couldn't get it to work on my previous attempt.
    # I feel like the approach was super similar but it was WAY slower and had some kind of error in it.
    # So I got some inspiration by nthistle.
    while True:
        (cy, cx), time, se, ss = nxt.popleft()
        if (cy, cx) == p2 and se and ss:  # Found the goal!
            t2 = time
            break

        # Keep track of current storms
        if time > max_time:
            max_time = time
            next_B()
            BC = get_B_set()

        for _,d in dirs.items():
            dy, dx = d
            ny = cy + dy
            nx = cx + dx
            n = ((ny, nx), time + 1, se, ss)

            # If out of bounds or in storm or already seen, discard
            if (ny, nx) in BC or n in seen or ((not (0 < ny <= h) or not (0 < nx <= w)) and (ny, nx) != p1 and (ny, nx) != p2):
                continue
            seen.add(n)

            if (ny, nx) == p2 and not se:
                n = ((ny, nx), time + 1, True, ss)
                if t == 0:
                    t = time + 1
            elif (ny, nx) == p1 and se:
                n = ((ny, nx), time + 1, se, True)

            nxt.append(n)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
    a1 = 18
    a2 = 54
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()


