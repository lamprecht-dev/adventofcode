from utils import *


def solve(d):
    t = 0
    t2 = 0

    G = grid(d)
    s = len(G)
    can_see_edge = []
    can_see_trees = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(s):
        edge_vals = []
        tree_counts = []
        for col in range(s):
            edge = False
            counts = [0 for _ in range(4)]

            for d in range(len(dirs)):
                dir = dirs[d]
                for di in range(1, s):
                    dr, dc = dir[0] * di, dir[1] * di
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < s) or not (0 <= nc < s):
                        # Outside
                        edge = True
                        break
                    counts[d] += 1
                    if int(G[nr][nc]) >= int(G[row][col]):
                        # Blocked
                        break
            edge_vals.append(edge)
            tree_counts.append(math.prod(counts))
        can_see_edge.append(edge_vals)
        can_see_trees.append(tree_counts)


    for r in can_see_edge:
        for c in r:
            t += int(c)

    for r in can_see_trees:
        t2 = max(max(r), t2)

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """30373
25512
65332
33549
35390"""
    a1 = 21
    a2 = 8
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



