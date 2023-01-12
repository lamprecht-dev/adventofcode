from utils import *


class Priority:
    def __init__(self):
        self.states = []
        self.priorities = []    # matches id in states
        self.his = []           # matches id in states
        self.visited = set()

    def add(self, mana_spend, state, his):
        if state in self.visited:
            return
        self.states.append(state)
        self.priorities.append(mana_spend)
        self.his.append(his)

    # VERY COSTLY! Potentially need to optimize with HEAP
    def pop(self):
        m = min(self.priorities)
        i = self.priorities.index(m)
        s = self.states[i]
        his = self.his.pop(i)
        self.states.remove(s)
        self.priorities.remove(m)
        self.visited.add(s)
        return m, s, his

    # Also costly, but not really changable with heap
    def update(self, mana_spend, state, his):
        if state not in self.states:
            self.add(mana_spend, state, his)
            return
        i = self.states.index(state)
        self.priorities[i] = min(self.priorities[i], mana_spend)
        self.his[i] = his  # BETTER HISTORY

    def empty(self):
        return len(self.states) == 0


def spell(s, spell): # php, bhp, mana, shield_timer, poison_timer, recharge_timer
    pmod = int(s[4] > 0) * 3
    rmod = int(s[5] > 0) * 101
    ns = max(s[3] - 1, 0)
    np = max(s[4] - 1, 0)
    nr = max(s[5] - 1, 0)

    #(s[0], s[1] - pmod, s[2] + rmod, ns, np, nr)
    if spell == "mm":  # Magic Missile
        return 53, (s[0], s[1] - 4 - pmod, s[2] - 53 + rmod, ns, np, nr)
    if spell == "d":  # Drain
        return 73, (s[0] + 2, s[1] - 2 - pmod, s[2] - 73 + rmod, ns, np, nr)
    if spell == "s" and ns == 0:  # Shield
        return 113, (s[0], s[1] - pmod, s[2] - 113 + rmod, 6, np, nr)
    if spell == "p" and np == 0:  # Poison
        return 173, (s[0], s[1] - pmod, s[2] - 173 + rmod, ns, 6, nr)
    if spell == "r" and nr == 0:  # Recharge
        return 229, (s[0], s[1] - pmod, s[2] - 229 + rmod, ns, np, 5)
    if spell == "boss":  # Boss Attack
        smod = int(s[3] > 0) * 7
        d = max(1, dmg - smod)
        return 0, (s[0] - d, s[1] - pmod, s[2] + rmod, ns, np, nr)

    return -1, None


dmg = 1

def solve(d, hard_mode = False):
    global dmg
    t = 0

    ww = words(d)
    dmg = int(ww[1][1])

    P = Priority()
    # mana spend, ( php, bhp, mana, shield_timer, poison_timer, recharge_timer)
    P.add(0, (50, int(ww[0][2]), 500, 0, 0, 0), [])

    while not P.empty():
        m, s, his = P.pop()  # get min mana spend state

        # P1: R P S MM MM P MM MM
        # P2: P R S P R D P D

        if hard_mode:
            if s[0] <= 1:
                continue
            s = (s[0] - 1, s[1], s[2], s[3], s[4], s[5])

        spells = ["mm", "d", "s", "p", "r"]
        for spell_cast in spells:
            nm, ns = spell(s, spell_cast)
            if nm == -1 or ns[2] < 0:
                continue

            if ns[1] <= 0:
                t = m + nm
                break

            _, ns2 = spell(ns, "boss")

            if ns2[1] <= 0:
                t = m + nm
                break
            if ns2[0] <= 0:
                continue

            # Update or add
            P.update(m + nm, ns2, his + [spell_cast])

        if t != 0:
            break

    return t # 953 too low


def main():
    solution = solve("""Hit Points: 55
Damage: 8""", False)  # HARD MODE
    print(BColors.HEADER + "Solutions" + BColors.ENDC)
    print(solution)


if __name__ == '__main__':
    main()
