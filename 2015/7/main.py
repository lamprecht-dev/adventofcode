import functools

from utils import *

Wires = {}


@functools.lru_cache(maxsize=None)
def resolve_circuit(w):
    if isinstance(w, int):
        return w
    wire = Wires[w]

    if wire[0] == "":
        return resolve_circuit(wire[1])
    if wire[0] == "NOT":
        return ~ resolve_circuit(wire[1])
    if wire[0] == "OR":
        return resolve_circuit(wire[1]) | resolve_circuit(wire[2])
    if wire[0] == "AND":
        return resolve_circuit(wire[1]) & resolve_circuit(wire[2])
    if wire[0] == "LSHIFT":
        return resolve_circuit(wire[1]) << resolve_circuit(wire[2])
    if wire[0] == "RSHIFT":
        return resolve_circuit(wire[1]) >> resolve_circuit(wire[2])

    return w


def solve(d):
    ww = words(d)

    def get_int(inp):
        if inp.isnumeric():
            return int(inp)
        return inp

    for word in ww:
        if len(word) == 3:
            Wires[word[2]] = ("", get_int(word[0]))
        elif len(word) == 4:
            Wires[word[3]] = (word[0], get_int(word[1]))
        else:
            Wires[word[4]] = (word[1], get_int(word[0]), get_int(word[2]))

    t = resolve_circuit('a')
    Wires['b'] = ("", t)
    resolve_circuit.cache_clear()
    t2 = resolve_circuit('a')

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()
