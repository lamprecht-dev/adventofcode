from utils import *


def solve(d):
    coords = [(0, 0)]
    coords1 = [(0, 0)]
    coords2 = [(0, 0)]
    directions = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
    i = 0

    for dir in list(d):
        coords.append((coords[-1][0] + directions[dir][0], coords[-1][1] + directions[dir][1]))
        if i % 2 == 0:
            coords1.append((coords1[-1][0] + directions[dir][0], coords1[-1][1] + directions[dir][1]))
        else:
            coords2.append((coords2[-1][0] + directions[dir][0], coords2[-1][1] + directions[dir][1]))
        i += 1

    t = len(set(coords))
    t2 = len(set(coords1 + coords2))

    return t, t2


def main():
    # Times: 4:50.25 and 7:00.44
    solutions = solve(inp())
    print("Solutions")
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
