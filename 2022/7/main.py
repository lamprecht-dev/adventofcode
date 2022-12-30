import collections as coll

from utils import *


def solve(d):
    t = 0

    ww = words(d)
    dirs = coll.defaultdict(int)
    cur_dir = coll.deque()
    for line in ww:
        if line[1] == "ls":
            continue
        if line[1] == "cd":
            if line[2] == "..":
                cur_dir.pop()
            elif line[2] == "/":
                cur_dir.clear()
                cur_dir.append("root")
            else:
                cur_dir.append(line[2])
        elif line[0] != "dir":
            size = int(line[0])
            cur_dirs_copy = cur_dir.copy()
            while len(cur_dirs_copy) > 0:
                d = "/".join(cur_dirs_copy)
                dirs[d] += size
                cur_dirs_copy.pop()

    disc_size = 70000000
    disc_space_needed = 30000000
    disc_space_left = disc_size - dirs['root']
    need_to_free = disc_space_needed - disc_space_left

    t2 = math.inf
    for key, val in dirs.items():
        if val <= 100000:
            t += val
        if val < need_to_free:
            continue
        t2 = min(val, t2)

    return t, t2


def main():
    if test():
        solutions = solve(inp())
        print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
        for s in solutions:
            print(s)
    else:
        print("\n\n" + BColors.FAIL + "Not All Test Successful" + BColors.ENDC)


def test():
    s = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    a1 = 95437
    a2 = 24933642
    return validate_solution(solve(s), (a1, a2))


if __name__ == '__main__':
    main()



