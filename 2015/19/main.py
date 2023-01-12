import collections as coll

from utils import *


def find_options(cur):
    options = set()
    for i in range(len(cur)):
        if cur[i:i+2] in ins:
            for ii in ins[cur[i:i+2]]:
                options.add(cur[0:i] + ii + cur[i + 2:])
        if cur[i] in ins:
            for ii in ins[cur[i]]:
                options.add(cur[0:i] + ii + cur[i+1:])
    return options


ins = coll.defaultdict(list)

def solve(d):
    global ins
    ins = coll.defaultdict(list)
    target = ""

    ww = words(d)
    for line in ww:
        if len(line) == 0:
            continue
        if len(line) == 1:
            target = line[0]
            break
        ins[line[0]].append(line[2])

    # I at first did a brute force and it didn't work. I got insipired by some reddit comments which are genious!
    # A few simple obversavtions are important. Lets call any molecul X except of Rn, Ar and Y,
    # which are special moleculs that are used to build other moleculs.
    # We either produce X => XX
    # Or we produce a complicated X => X RN X AR | X => X RN X Y X AR | X => X => X RN X Y X Y X AR
    # We can simplify this by calling it X=>X(X) ; X=>X(X,X) ; X=> X(X,X,X)
    # So in the simple case we reduce per step by 1 and in the complicated case we reduce by 3,5 or 7
    # XXX => X are two steps. X => e is one step, so if we just have some amount of X, that amount is the amount of steps
    # But we can reduce the amount of steps depending on ( and ,
    # For ( we get from 4,6,8 mols to 1, depending on the amount of , (in one step)
    # X(X,X,X)X = 3 steps, X(X,X,X)=>X : 1, XX => e : 2
    # X(X,X)X = 3 steps, X(X,X)=>X : 1, XX => e : 2
    # X(X)X = 3 steps, X(X)=>X : 1, XX => e : 2
    # So can we just count X and substract the amount of , ?

    simple_string = target.replace('Rn', "(")
    simple_string = simple_string.replace('Ar', ")")
    simple_string = simple_string.replace('Y', ",")
    for i in ins:
        simple_string = simple_string.replace(i, 'X')

    return len(find_options(target)), \
           simple_string.count('X') - simple_string.count(',') - int(simple_string.count(',') != 0)  #207


def main():
    if test():
        solutions = solve(inp())
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    s = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""

    a1 = 7
    a2 = 6
    return validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()
