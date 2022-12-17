from utils import *


def bfs(grid, start, end, w, h):
    to_check = start
    steps = [0] * len(start)
    checked = []
    searching = True

    while searching:
        if len(to_check) == 0:
            return 0

        c = to_check.pop(0)
        c_step = steps.pop(0)
        c_val = grid[c]

        if c == end:
            return c_step

        # go up
        n = c - w
        if n >= 0 and grid[n] - 1 <= c_val and n not in checked and n not in to_check:
            to_check.append(n)
            steps.append(c_step + 1)

        # go down
        n = c + w
        if n < w * h and grid[n] - 1 <= c_val and n not in checked and n not in to_check:
            to_check.append(n)
            steps.append(c_step + 1)

        # go left
        n = c - 1
        if n >= 0 and c % w != 0 and grid[n] - 1 <= c_val and n not in checked and n not in to_check:
            to_check.append(n)
            steps.append(c_step + 1)

        # go up
        n = c + 1
        if n >= 0 and c % w != w - 1 and grid[n] - 1 <= c_val and n not in checked and n not in to_check:
            to_check.append(n)
            steps.append(c_step + 1)

        checked.append(c)
    return 0


def solve(d):
    ll = lines(d)
    flat_grid = []
    start = -1
    starts = []
    end = -1
    w = len(ll[0])
    h = len(ll)
    i = 0

    for l in ll:
        for s in l:
            val = ord(s) - 97
            if val == -28:  # end
                end = i
                flat_grid.append(ord('z') - 97)
            elif val == -14:  # start
                start = i
                flat_grid.append(0)
            else:
                flat_grid.append(val)
                if val == 0:
                    starts.append(i)
            i += 1

    t = bfs(flat_grid, [start], end, w, h)
    t2 = bfs(flat_grid, starts, end, w, h)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    a1 = 31
    a2 = 29
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



