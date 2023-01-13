from utils import *


def solve(d, a=0):
    ww = words(d)
    pointer = 0
    reg = {'a': a, 'b': 0}
    while pointer < len(ww):
        if pointer < 0:
            break
        w = ww[pointer]
        if w[0] == "hlf":
            reg[w[1]] //= 2
        elif w[0] == "tpl":
            reg[w[1]] *= 3
        elif w[0] == "inc":
            reg[w[1]] += 1
        elif w[0] == "jmp":
            pointer += int(w[1])
            continue
        elif w[0] == "jie" and reg[w[1][:-1]] % 2 == 0:
            pointer += int(w[2])
            continue
        elif w[0] == "jio" and reg[w[1][:-1]] == 1:
            pointer += int(w[2])
            continue
        pointer += 1

    t = reg['b']

    return t


def main():
    solution = solve(inp(), 1)
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    print(solution)


if __name__ == '__main__':
    main()
