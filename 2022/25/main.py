from utils import *

max_mem = {0: 2}

def get_max(d):
    if d < 0:
        return 0
    if d in max_mem:
        return max_mem[d]
    for i in range(d + 1):
        if i not in max_mem:
            max_mem[i] = max_mem[i - 1] + (pow(5, i) * 2)
    return max_mem[d]


def to_SNAFU(d):
    i = 0
    while True:
        max_i = get_max(i)
        if max_i > d:
            break
        i += 1

    a = ""
    for j in range(i + 1):  # Iterate through all places
        max_before = get_max(i - j - 1)
        if d > 0:
            if max_before >= d:
                a += "0"
            elif max_before + pow(5, i - j) < d:
                d -= pow(5, i - j) * 2
                a += "2"
            else:
                d -= pow(5, i - j)
                a += "1"
        elif d < 0:
            if -max_before <= d:
                a += "0"
            elif - max_before - pow(5, i - j) > d:
                d += pow(5, i - j) * 2
                a += "="
            else:
                d += pow(5, i - j)
                a += "-"
        else:
            a += "0"
    return a


def to_dec(d):
    convert = {"-" : -1, "=" : -2, "0": 0, "1": 1, "2": 2}
    d = list(d)
    sum = 0
    for i in range(len(d)):
        place = len(d) - i - 1
        val = convert[d[i]]
        sum += pow(5, place) * val
    return sum


def solve(d):
    ll = lines(d)
    sum = 0
    for l in ll:
        dec = to_dec(l)
        sum += dec

    t = to_SNAFU(sum)
    return t


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    print(solutions)


def test():
    s = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
    a1 = "2=-1=0"
    validate_solution([solve(s)], [a1])


if __name__ == '__main__':
    main()



