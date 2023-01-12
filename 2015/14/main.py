from utils import *


def dist_after(time, v, vt, rt):
    cycle_dist = v * vt
    cycle_time = vt + rt
    cycles = time // cycle_time
    rem = time - (cycles * cycle_time)
    rem_dist = min(vt, rem) * v
    return rem_dist + (cycles * cycle_dist)


def solve(d):
    t = 0

    ww = words(d)
    limit = 2503
    deers = []
    for line in ww:
        dstats = int(line[3]), int(line[6]), int(line[13])
        deers.append(dstats)

        t = max(t, dist_after(limit, *dstats))

    scores = [0] * len(deers)
    for i in range(1, limit + 1):
        best_dist = 0
        best_deer = []
        for di in range(len(deers)):
            dist = dist_after(i, *deers[di])
            if dist > best_dist:
                best_deer = [di]
                best_dist = dist
            elif dist == best_dist:
                best_deer.append(di)

        for di in best_deer:
            scores[di] += 1

    t2 = max(scores)

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
