from utils import *


class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

    def add_next(self, n):
        self.next = n

    def insert(self, n):  # Insert after self
        n.next = self.next
        n.prev = self
        if self.next is not None:
            self.next.prev = n
        self.next = n

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        return self


def solve(d, p=1):
    original = ints(d)
    head = None
    tail = None
    reference = []
    key = 811589153 if p == 2 else 1

    for o in original:
        n = Node(o * key)
        reference.append(n)
        if head is None:
            head = n
        else:
            tail.insert(n)

        tail = n
    tail.next = head
    head.prev = tail

    for its in range(10 if p == 2 else 1):
        for r in reference:
            if r.val == 0:
                continue
            r.remove()
            c = r
            move = r.val % (len(reference) - 1)
            for _ in range(abs(move)):
                c = c.next
            c.insert(r)

    t = []
    for i in range(3):
        c = head
        while c.val != 0:
            c = c.next
        for _ in range((i + 1) * 1000):
            c = c.next
        t.append(c.val)

    return sum(t), t


def main():
    test()
    solutions = (solve(inp())[0], solve(inp(), 2)[0])
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


def test():
    s = """1
2
-3
3
-2
0
4"""
    a1 = 3
    a2 = 1623178306
    validate_solution((solve(s)[0], solve(s, 2)[0]), (a1, a2))


if __name__ == '__main__':
    main()



