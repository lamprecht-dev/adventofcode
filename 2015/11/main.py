from utils import *


def is_correct(pswd):

    first_pair = -1
    second_pair = -1
    got_cont = False
    for i in range(len(pswd)):
        p = pswd[i]
        if p in [8, 14, 11]:
            return False
        if i < len(pswd) - 1:
            if pswd[i] == pswd[i + 1]:
                if first_pair == -1:
                    first_pair = i
                elif first_pair < i - 1:
                    second_pair = i
        if i < len(pswd) - 2:
            if pswd[i + 2] - 2 == pswd[i + 1] - 1 == pswd[i]:
                got_cont = True
    return got_cont and first_pair != -1 and second_pair != -1


def inc(pswd):
    for i in range(len(pswd)):
        ni = len(pswd) - i - 1
        pswd[ni] += 1
        if pswd[ni] < 26:
            break
        else:
            pswd[ni] -= 26
    return pswd

def solve(d):
    t = ""

    pswd = []

    for c in d:
        pswd.append(ord(c) - 97)

    valid_pair = False
    while not valid_pair:
        pswd = inc(pswd)
        valid_pair = is_correct(pswd)

    for p in pswd:
        t += chr((p + 97))

    return t, 0


def main():
    if test():
        solutions = solve('vzbxxyzz') # I simply inserted the second password
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    return validate_solution(solve('abcdefgh'), ('abcdffaa', 0))


if __name__ == '__main__':
    main()

