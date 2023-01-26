import hashlib


from utils import *


def solve(d):
    t = ""
    t2 = [''] * 8

    i = 0
    indexed = set()
    while len(t) < 8 or len(indexed) < 8:
        md5 = hashlib.md5((d + str(i)).encode()).hexdigest()
        if md5[:5] == "00000":
            if len(t) < 8:
                t += md5[5]
            if md5[5].isnumeric() and int(md5[5]) in range(8) and int(md5[5]) not in indexed:
                t2[int(md5[5])] = md5[6]
                indexed.add(int(md5[5]))
        i += 1

    return t, ''.join(t2)


def main():
    if test():
        solutions = solve(inp())
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    s = """abc"""
    a1 = '18f47a30'
    a2 = '05ace8e3'
    return validate_solution(solve(s), (a1, a2))


main()
