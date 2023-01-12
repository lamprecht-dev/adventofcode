def get_house(target, limit=None, mult=10):
    t = target // 10
    house = [0] * t

    for i in range(1, t):
        c = 0
        for j in range(i, t, i):
            if limit is not None:
                if c >= limit:
                    break
                c += 1
            house[j] += i * mult

    for h in house:
        if h >= target:
            return house.index(h)


def solve(d):
    t = get_house(d)
    t2 = get_house(d, 50, 11)

    return t, t2


def main():
    solutions = solve(34000000)
    print("Solutions")
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()

