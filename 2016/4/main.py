import collections as coll

from utils import *


def solve(d):
    t = 0
    t2 = 0

    ww = words(d, "-")
    for line in ww:
        counter = coll.Counter()
        id, checksum = line[-1].split('[')
        checksum = checksum[:-1]
        
        for l in line[:-1]:
            counter.update(list(l))
        mc = counter.most_common()
        prev = math.inf
        prev_set = set()
        my_checksum = ""
        for m in mc:
            if m[1] < prev:
                possible = sorted(list(prev_set))
                if len(possible) < 5 - len(my_checksum):
                    my_checksum += "".join(possible)
                else:
                    my_checksum += "".join(possible[:5 - len(my_checksum)])
                
                prev = m[1]
                prev_set = set(m[0])
                if len(my_checksum) == 5:
                    break
            else:
                prev_set.add(m[0])

        if len(my_checksum) < 5:
            possible = sorted(list(prev_set))
            my_checksum += "".join(possible[:5 - len(my_checksum)])

        # 97 - 122
        if my_checksum == checksum:
            t += int(id)
            room_name = ""
            for l in line[:-1]:
                for c in l:
                    cint = ord(c) + (int(id) % 26)
                    while cint > 122:
                        cint -= 26
                    room_name += chr(cint)
                room_name += " "
            if room_name == "northpole object storage ":
                t2 = int(id)

    return t, t2


def main():
    solutions = solve(inp())
    print("\n\n" + BColors.HEADER + "Solutions" + BColors.ENDC)
    for s in solutions:
        print(s)


main()
