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


def grid(s):
    return [list(x) for x in s.split("\n")]


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
    all_valid = True
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
            all_valid = False
    return all_valid


class Grid:
    def __init__(self, default_value=""):
        self.default_value = default_value
        self.w = 0
        self.h = 0
        self.G = []

    def set_default_value(self, default_value=""):
        self.default_value = default_value

    def get(self, c: int, r: int):
        if c >= self.w or r >= self.h:
            return self.default_value
        return self.G[r][c]

    def fill(self, c: int, r: int):
        if c >= self.w:
            for rr in range(self.h):
                for ci in range(self.w, c + 1):
                    self.G[rr].append(self.default_value)
            self.w = c + 1
        if r >= self.h:
            for _ in range(self.h, r + 1):
                self.G.append([self.default_value] * self.w)
            self.h = r + 1

    def set(self, c: int, r: int, value):
        self.fill(c, r)
        self.G[r][c] = value

    def literal_print(self, swap_coords=False):
        if swap_coords:
            for c in range(self.w):
                row = ""
                for r in range(self.h):
                        row += self.G[r][c]
                print(row)
        else:
            for r in range(self.h):
                row = ""
                for c in range(self.w):
                        row += self.G[r][c]
                print(row)

    def get_non_default_values(self):
        values = []
        for r in range(self.h):
            for c in range(self.w):
                if self.G[r][c] != self.default_value:
                    value_location = {'r': r, 'c': c, 'v': self.G[r][c]}
                    values.append(value_location)
        return values


class Tree:
    def __init__(self, value="", parent=None):
        self.value = value
        self.children = []
        self.parent = parent

    def insert_child(self, value="", index=-1):
        t = Tree(value, self)

        if index < 0:
            index = len(self.children) + index
            if index < 0:
                index = 0
        self.children.insert(index, t)

    def is_leaf(self):
        return len(self.children) == 0

    def get_siblings(self):
        if self.parent is None:
            return None

        siblings = []

        ch = self.parent.children
        for c in ch:
            if c is not self:
                siblings.append(c)

        return siblings
