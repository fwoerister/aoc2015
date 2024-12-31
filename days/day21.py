from heapq import heappop, heappush

from util.solution import SolutionBase

items = [
    ('w', 8, 4, 0),
    ('w', 10, 5, 0),
    ('w', 25, 6, 0),
    ('w', 40, 7, 0),
    ('w', 74, 8, 0),
    ('a', 13, 0, 1),
    ('a', 31, 0, 2),
    ('a', 53, 0, 3),
    ('a', 75, 0, 4),
    ('a', 102, 0, 5),
    ('r', 25, 1, 0),
    ('r', 50, 2, 0),
    ('r', 100, 3, 0),
    ('r', 20, 0, 1),
    ('r', 40, 0, 2),
    ('r', 80, 0, 3),
]


def get_weapon_count(items):
    return len([i for i in items if i[0] == 'w'])


def get_armour_count(items):
    return len([i for i in items if i[0] == 'a'])


def get_ring_count(items):
    return len([i for i in items if i[0] == 'r'])


def evaluate_winner(player, boss):
    p_hit, p_damage, p_armour = player
    b_hit, b_damage, b_armour = boss

    b_reduction = p_damage - b_armour if (p_damage - b_armour) > 0 else 1
    p_reduction = b_damage - p_armour if (b_damage - p_armour) > 0 else 1

    p_cycles = p_hit // p_reduction
    b_cycles = b_hit // b_reduction

    if p_cycles >= b_cycles:
        return 'player'
    return 'boss'


def equipe_player(player, items):
    h, d, a = player

    d += sum([d for t, g, d, a in items])
    a += sum([a for t, g, d, a in items])

    return h, d, a


def find_best_equipment(player, boss, equipment, items):
    open_solutions = [(0, [], list(items))]

    while open_solutions:
        c, e, i = heappop(open_solutions)

        if not i:
            continue

        if get_ring_count(e) > 2:
            continue

        if get_armour_count(e) > 1:
            continue

        if get_weapon_count(e) > 1:
            continue

        if get_weapon_count(e) == 1 and evaluate_winner(equipe_player(player, e), boss) == 'player':
            return c

        i_t, i_c, i_d, i_a = i[0]
        heappush(open_solutions, (c + i_c, e + [i[0]], i[1:]))
        heappush(open_solutions, (c, e, i[1:]))


def find_most_expensive_equipment(player, boss, equipment, items):
    open_solutions = [(0, [], list(items))]
    max_expense = 0

    while open_solutions:
        c, e, i = heappop(open_solutions)

        if not i:
            continue

        if get_ring_count(e) > 2:
            continue

        if get_armour_count(e) > 1:
            continue

        if get_weapon_count(e) > 1:
            continue

        if get_weapon_count(e) == 1 and evaluate_winner(equipe_player(player, e), boss) == 'player':
            continue
        if get_weapon_count(e) == 1 and evaluate_winner(equipe_player(player, e), boss) == 'boss':
            if max_expense < c:
                max_expense = c

        i_t, i_c, i_d, i_a = i[0]
        heappush(open_solutions, (c + i_c, e + [i[0]], i[1:]))
        heappush(open_solutions, (c, e, i[1:]))

    return max_expense


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 21)

    def level1(self, example_input=False):
        items.sort(key=lambda item: item[1])
        return find_best_equipment((100, 0, 0), (100, 8, 2), [], items)

    def level2(self, example_input=False):
        items.sort(key=lambda item: item[1])
        return find_most_expensive_equipment((100, 0, 0), (100, 8, 2), [], items)
