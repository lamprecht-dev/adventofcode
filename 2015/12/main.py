import json
import re
from utils import *


def sum_not_red(obj):
    s = 0
    if isinstance(obj, dict):
        for key, val in obj.items():
            if val == 'red':
                return 0
            s += sum_not_red(val)
    elif isinstance(obj, list):
        for i in obj:
            s += sum_not_red(i)
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0

    return s


def solve(d):
    result = [int(n) for n in re.findall(r'-?\d+', d)]
    t = sum(result)

    obj = json.loads(d)
    t2 = sum_not_red(obj)

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    main()



