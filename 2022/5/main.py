import copy
import re

from utils import *


def solve(d):
    origianl_containers = []
    procedure = []

    step = 0

    for line in lines(d):
        if step == 0:
            for i in range(1, len(line), 4):
                if len(origianl_containers) < i // 4 + 1:
                    origianl_containers.append([])
                if line[i:i + 1] != " " and line[i:i + 1].isdigit() is False:
                    origianl_containers[i // 4].append(line[i:i + 1])
            if len(line) == 0:
                step += 1
        else:
            procedure += [tuple([int(x) for x in re.findall(r'\d+', line)])]

    containers = copy.deepcopy(origianl_containers)
    for prod in procedure:
        from_container = prod[1] - 1
        to_container = prod[2] - 1
        items = []
        for i in range(prod[0]):
            item = containers[from_container].pop(0)
            containers[to_container].insert(0, item)
            items.append(origianl_containers[from_container].pop(0))

        origianl_containers[to_container] = items + origianl_containers[to_container]

    t = ""
    t2 = ""

    for cont in containers:
        t += cont[0]

    for cont in origianl_containers:
        t2 += cont[0]

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    a1 = "CMZ"
    a2 = "MCD"
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



