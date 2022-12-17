import math


def ints(s, sep=None):
    if isinstance(s, str):
        return [int(x) for x in s.split(sep)]
    else:
        return [int(x) for x in s]


def words(s, sep=None):
    if isinstance(s, str):
        return [[x for x in l.split(sep)] for l in s.split("\n")]
    else:
        pass  # TODO: Need to make a usecase


def lines(s):
    return [l for l in s.split("\n")]


def stats(d, sep=None):
    s = d.replace("\n", "")
    total_length = len(s)

    ll = lines(d)
    row_count = len(ll)
    shortest_row = math.inf
    longest_row = -math.inf
    least_words = math.inf
    most_words = -math.inf

    for l in ll:
        shortest_row = min(shortest_row, len(l))
        longest_row = max(longest_row, len(l))

        ww = l.split(sep)
        least_words = min(least_words, len(ww))
        most_words = max(most_words, len(ww))

    print("Total Length: ", total_length)
    print("Row Count: ", row_count)
    print("Shortest Row: ", shortest_row)
    print("Longest Row: ", longest_row)
    print("Least Words: ", least_words)
    print("Most Words: ", most_words)


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def inp(filepath='./input.txt'):
    with open(filepath) as f:
        data = f.read()

    return data


def validate_solution(my_solutions, intended_solutions):
    print(BColors.HEADER + "Validation" + BColors.ENDC)
    for i in range(len(my_solutions)):
        print("\nSolution Nr ", i+1)

        is_valid = my_solutions[i] == intended_solutions[i]
        if is_valid:
            print(my_solutions[i])
            print(BColors.OKGREEN + str(is_valid) + BColors.ENDC)
        else:
            print("My Solution")
            print(my_solutions[i])
            print("Actual Solution")
            print(intended_solutions[i])
            print(BColors.FAIL + str(is_valid) + BColors.ENDC)