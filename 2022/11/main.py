import copy
import re
from utils import *


def monkey_business(monkeys, rounds, less_worried=True):
    lcm = 1
    for m in monkeys:
        lcm *= m['test']  # Idea from @jonathanpaulson
    for r in range(rounds):  # For each round
        for m in monkeys:  # For each monkey
            m['count'] += len(m['items'])
            for old in m['items']:  # For each item / old is needed for eval!!
                new = eval(m['op'])
                if less_worried:
                    new = new // 3
                else:
                    new %= lcm
                monkeys[m[new % m['test'] == 0]]['items'].append(new)
            m['items'] = []

    inspect_counts = []
    for m in monkeys:
        inspect_counts.append(m['count'])
    return inspect_counts


def solve(d):
    monkeys = []

    for block in d.split("\n\n"):
        ll = block.split("\n")
        monkey = {
            'items': ints(ll[1].replace("  Starting items: ", ""), ", "),
            'op': ll[2].replace("  Operation: new = ", ""),
            'test': int(re.findall(r'\d+', ll[3])[0]),
            True: int(re.findall(r'\d+', ll[4])[0]),
            False: int(re.findall(r'\d+', ll[5])[0]),
            'count': 0
        }
        monkeys.append(monkey)

    inspect_counts = monkey_business(copy.deepcopy(monkeys), 20)
    inspect_counts.sort(reverse=True)
    t = math.prod(inspect_counts[:2])

    inspect_counts = monkey_business(monkeys, 10000, False)
    inspect_counts.sort(reverse=True)
    t2 = math.prod(inspect_counts[:2])

    return t, t2


def main():
    test()
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    a1 = 10605
    a2 = 2713310158
    validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



