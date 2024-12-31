from heapq import heappop, heappush

from util.solution import SolutionBase


def find_cheapest_win(player, boss, hard_mode=False):
    p_h, p_m, p_a = player
    b_h, b_d, b_a = boss

    open_solutions = [(0, 'p', p_m, p_h, b_h, 0, 0, 0)]

    while open_solutions:
        mana_spent, turn, mana, p_hit, b_hit, shield, poison, recharge = heappop(open_solutions)

        if hard_mode and turn == 'p':
            p_hit -= 1

        if poison > 0:
            b_hit -= 3

        if recharge > 0:
            mana += 101

        if p_hit <= 0:
            continue

        if b_hit <= 0:
            return mana_spent

        if mana < 53:
            continue

        if turn == 'p':
            # magic missile
            if mana >= 53:
                heappush(open_solutions, (mana_spent + 53,
                                          'b',
                                          mana - 53,
                                          p_hit,
                                          b_hit - 4,
                                          shield - 1 if shield > 0 else 0,
                                          poison - 1 if poison > 0 else 0,
                                          recharge - 1 if recharge > 0 else 0))
            # drain
            if mana >= 73:
                heappush(open_solutions, (mana_spent + 73,
                                          'b',
                                          mana - 73,
                                          p_hit + 2,
                                          b_hit - 2,
                                          shield - 1 if shield > 0 else 0,
                                          poison - 1 if poison > 0 else 0,
                                          recharge - 1 if recharge > 0 else 0))

            # shield
            if mana >= 113 and shield <= 1:
                heappush(open_solutions, (mana_spent + 113,
                                          'b',
                                          mana - 113,
                                          p_hit,
                                          b_hit,
                                          6,
                                          poison - 1 if poison > 0 else 0,
                                          recharge - 1 if recharge > 0 else 0))

            # poison
            if mana >= 173 and poison <= 1:
                heappush(open_solutions, (mana_spent + 173,
                                          'b',
                                          mana - 173,
                                          p_hit,
                                          b_hit,
                                          shield - 1 if shield > 0 else 0,
                                          6,
                                          recharge - 1 if recharge > 0 else 0))
            # recharge
            if mana >= 229 and recharge <= 1:
                heappush(open_solutions, (mana_spent + 229,
                                          'b',
                                          mana - 229,
                                          p_hit,
                                          b_hit,
                                          shield - 1 if shield > 0 else 0,
                                          poison - 1 if poison > 0 else 0,
                                          5))
        else:
            current_player_armour = p_a
            if shield > 0:
                current_player_armour += 7

            damage = b_d - current_player_armour

            if damage <= 0:
                damage = 1

            heappush(open_solutions, (mana_spent,
                                      'p',
                                      mana,
                                      p_hit - damage,
                                      b_hit,
                                      shield - 1 if shield > 0 else 0,
                                      poison - 1 if poison > 0 else 0,
                                      recharge - 1 if recharge > 0 else 0))


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 22)

    def level1(self, example_input=False):
        return find_cheapest_win((50, 500, 0), (55, 8, 0))

    def level2(self, example_input=False):
        return find_cheapest_win((50, 500, 0), (55, 8, 0), True)
