import sympy as sp

from utils import *

class Node:
    def __init__(self, name=None):
        self.name = name
        self.parents = []
        self.val = None
        self.left = None
        self.right = None
        self.leftv = None
        self.rightv = None
        self.op = None

    def get_expression(self, ins):
        if self.name == "humn" and self.val is None:
            return 'humn'
        elif self.op == "=":
            return ins[self.left].get_expression(ins) + "-" + ins[self.right].get_expression(ins)
        elif self.op is not None:
            return "(" + ins[self.left].get_expression(ins) + self.op + ins[self.right].get_expression(ins) + ")"
        else:
            return str(self.val)


def solve(d):
    instructions = {}
    needs_solving = []

    ww = words(d)
    for line in ww:
        line[0] = line[0][0:-1]
        needs_solving.append(line[0])
        if len(line) == 2:
            n = Node(line[0])
            n.val = int(line[1])
            instructions[line[0]] = n
        else:
            n = Node(line[0])
            n.left = line[1]
            n.right = line[3]
            n.op = line[2]
            instructions[line[0]] = n

    expression = instructions['root'].get_expression(instructions)
    t = sp.simplify(expression)

    instructions['root'].op = "="
    instructions['humn'].val = None

    expression = instructions['root'].get_expression(instructions)
    t2 = sp.solve(expression, "humn")[0]

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
    a1 = 152
    a2 = 301
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
