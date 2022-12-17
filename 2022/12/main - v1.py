from utils import *


def d_alg(grid, start, end, w, h, exclude=None):
    if exclude is None:
        exclude = []
    to_check = [start]
    steps = [0]
    path = [[]]
    checked = []
    searching = True

    while searching:
        if len(to_check) == 0:
            return []

        c = to_check.pop(0)
        c_step = steps.pop(0)
        c_val = grid[c]
        c_path = path.pop(0)

        if c == end:
            return c_path

        # go up
        n = c - w
        if n >= 0 and grid[n] - 1 <= c_val and n not in checked and n not in to_check and n not in exclude:
            to_check.append(n)
            steps.append(c_step + 1)
            new_path = c_path[:]
            new_path.append(c)
            path.append(new_path)

        # go down
        n = c + w
        if n < w * h and grid[n] - 1 <= c_val and n not in checked and n not in to_check and n not in exclude:
            to_check.append(n)
            steps.append(c_step + 1)
            new_path = c_path[:]
            new_path.append(c)
            path.append(new_path)

        # go left
        n = c - 1
        if n >= 0 and c % w != 0 and grid[n] - 1 <= c_val and n not in checked and n not in to_check and n not in exclude:
            to_check.append(n)
            steps.append(c_step + 1)
            new_path = c_path[:]
            new_path.append(c)
            path.append(new_path)

        # go up
        n = c + 1
        if n >= 0 and c % w != w - 1 and grid[n] - 1 <= c_val and n not in checked and n not in to_check and n not in exclude:
            to_check.append(n)
            steps.append(c_step + 1)
            new_path = c_path[:]
            new_path.append(c)
            path.append(new_path)

        checked.append(c)

    return []


def solve(d):
    ll = lines(d)
    flat_grid = []
    start = -1
    other_starts = []
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
                    other_starts.append(i)
            i += 1

    path = d_alg(flat_grid, start, end, w, h)
    t = len(path)
    paths = [path]
    exclude = [start]

    t2 = math.inf
    for s in other_starts:
        exclude.append(s)
        shortest_p = []
        for p in paths:
            if s in p:
                np = p[p.index(s):]
                if len(np) < len(shortest_p):
                    shortest_p = np
        if len(shortest_p) == 0:
            p = d_alg(flat_grid, s, end, w, h, exclude)
            if len(p) != 0:
                paths.append(p)
        else:
            paths.append(shortest_p)

    for p in paths:
        t2 = min(t2, len(p))

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



