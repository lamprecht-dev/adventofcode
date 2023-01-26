import itertools as it

from utils import *



def abba(str):
    for i in range(len(str) - 3):
        if str[i] == str[i + 3] and str[i + 1] == str[i + 2] and str[i] != str[i + 1]:
            return True
    return False


def aba(str):
    aba = set()
    for i in range(len(str) - 2):
        if str[i] == str[i + 2] and str[i] != str[i + 1]:
            aba.add((str[i], str[i + 1]))
    return aba


def solve(d):
    t = 0
    t2 = 0
    
    ll = lines(d)
    for line in ll:
        s = line
        in_ins = False
        in_outs = False
        babs = set()
        abas = set()

        while '[' in s:        
            d1 = s.index('[')
            d2 = s.index(']')
            p1 = s[:d1]
            p2 = s[d1+1:d2]
            
            if abba(p1):
                in_outs = True
            if abba(p2):
                in_ins = True

            abas.update(aba(p1))
            babs.update(aba(p2))

            s = s[d2+1:]
        
        if abba(s):
            in_outs = True    
        abas.update(aba(s))

        if in_outs and not in_ins:
            t+=1

        found_match = False
        for a in abas:
            for b in babs:
                if a[0] == b[1] and a[1] == b[0]:
                    t2 += 1
                    found_match = True
                    break 
            if found_match:
                break
    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s) 

main()
