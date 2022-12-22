import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
# import bisect
# import heapq
# import sys
# sys.setrecursionlimit(1000000)

from utils import *

# TODO: CREATE CLASSES FOR VM, Tree, Graph etc

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


def solve(d):
    stats(d)
    print("Input: ", repr(d))
    t2 = 0

    instructions = {}

    ww = words(d)
    for line in ww:
        line[0] = line[0][0:-1]
        if len(line) == 2:
            n = Node()
            n.val = int(line[1])
            instructions[line[0]] = n
        else:
            n = Node()
            n.left = line[1]
            n.right = line[3]
            n.op = line[2]
            instructions[line[0]] = n

    next = ['root']
    done = []
    while len(next) > 0:
        c = instructions[next[-1]]

        # If we have a number, mark as done
        if c.val is not None:
            done.append(next[-1])
            next.pop()
            continue

        # If at least one of left or right does not have a node, add string to next and continue
        # If both have nodes, it means they are processed and we can get their values
        l = c.left
        r = c.right
        scount = 0
        if isinstance(l, str):
            c.left = instructions[l]
            next.append(l)
            scount += 1
        if isinstance(r, str):
            c.right = instructions[r]
            next.append(r)
            scount += 1
        if scount == 0:
            if c.op == "+":
                c.val = c.left.val + c.right.val
            if c.op == "-":
                c.val = c.left.val - c.right.val
            if c.op == "*":
                c.val = c.left.val * c.right.val
            if c.op == "/":
                c.val = c.left.val / c.right.val

    t = int(instructions['root'].val)

    return t, t2


def solve2(d):
    stats(d)
    print("Input: ", repr(d))
    t = 0
    t2 = 0

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
        if line[0] == "humn":
            n.val = None

    while len(needs_solving) > 0:
        for ns in needs_solving:
            if ns == "humn":
                if instructions[ns].val is None:
                    continue
                t2 = instructions[ns].val
                needs_solving = []
                break

            ins = instructions[ns]
            l = ins.left
            r = ins.right

            if len(needs_solving) <= 64:
                print([n.name for n in ins.parents], ins.name)

            # print(ns, ins.leftv, ins.op, ins.rightv, ins.val)
            count_parts = 0

            if ins.val is not None and isinstance(ins.val, (int, float)):
                count_parts += 1
            if ins.leftv is not None:
                count_parts += 1
            if ins.rightv is not None:
                count_parts += 1

            if count_parts == 3 or (count_parts == 1 and ins.val is not None):
                needs_solving.remove(ns)
            elif count_parts < 2:
                # print(ns, ins.leftv, ins.rightv, ins.val, len(needs_solving))
                if ns == 'root' and count_parts == 1:
                    if l.val is not None:
                        ins.right.val = l.val
                        ins.rightv = l.val
                        ins.val = l.val
                    if r.val is not None:
                        ins.left.val = r.val
                        ins.leftv = r.val
                        ins.val = r.val
                else:  # Not enough data yet
                    # print(ins.left, ns, ins.right, ins.val)
                    if isinstance(l, str):
                        ins.left = instructions[l]
                        ins.left.parents.append(ins)
                    elif l.val is not None and ins.leftv is None:
                        ins.leftv = l.val
                    if isinstance(r, str):
                        ins.right = instructions[r]
                        ins.right.parents.append(ins)
                    elif r.val is not None and ins.rightv is None:
                        ins.rightv = r.val
            else:
                if ins.val is None:
                    if ins.op == "+":
                        ins.val = ins.leftv + ins.rightv
                    if ins.op == "-":
                        ins.val = ins.leftv - ins.rightv
                    if ins.op == "*":
                        ins.val = ins.leftv * ins.rightv
                    if ins.op == "/":
                        ins.val = ins.leftv / ins.rightv
                elif ins.leftv is not None:  # case right
                    new_val = 0
                    if ins.op == "+":
                        new_val = ins.val - ins.leftv
                    if ins.op == "-":
                        new_val = ins.leftv - ins.val
                    if ins.op == "*":
                        new_val = ins.val / ins.leftv
                    if ins.op == "/":
                        new_val = ins.leftv / ins.val
                    ins.rightv = new_val
                    ins.right.val = new_val
                else:  # case left
                    new_val = 0
                    if ins.op == "+":
                        new_val = ins.val - ins.rightv
                    if ins.op == "-":
                        new_val = ins.rightv + ins.val
                    if ins.op == "*":
                        new_val = ins.val / ins.rightv
                    if ins.op == "/":
                        new_val = ins.rightv * ins.val
                    ins.leftv = new_val
                    ins.left.val = new_val

    return t, t2


def main():
    test()
    solutions = solve2(inp())
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
    a1 = 150
    a2 = 301
    validate_solution(solve2(s), (a1, a2))


if __name__ == '__main__':
    main()
