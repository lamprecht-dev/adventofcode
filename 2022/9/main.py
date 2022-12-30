from utils import *


def solve(d):
    H = [(0, 0)]
    T = [[(0, 0)] for _ in range(9)]

    DR = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    DC = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

    ww = [[x for x in l.split()] for l in d.split("\n")]
    for l in ww:
        for _ in range(int(l[1])):
            NH = (H[-1][0] + DC[l[0]], H[-1][1] + DR[l[0]])
            H.append(NH)

            for i in range(9):
                h = T[i - 1]
                t = T[i]
                if i == 0:
                    h = H
                T[i].append(get_new_pos(h[-1], t[-1]))

    t = len(set(T[0]))
    t2 = len(set(T[8]))

    return t, t2


def get_new_pos(H, T):
    NT = T
    y_diff = abs(T[0] - H[0])
    x_diff = abs(T[1] - H[1])
    y_dir = (H[0] - T[0]) // y_diff if y_diff != 0 else 0
    x_dir = (H[1] - T[1]) // x_diff if x_diff != 0 else 0
    if x_diff > 1 or y_diff > 1:
        NT = (T[0] + y_dir, T[1] + x_dir)

    return NT


if __name__ == '__main__':
    s = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    s2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    validate_solution(solve(s), (13, 1))    # Test 1
    validate_solution(solve(s2), (88, 36))  # Test 2
    validate_solution(solve(inp()), (6243, 2630))   # Main Puzzle



