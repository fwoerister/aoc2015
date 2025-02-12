import re

from util.solution import SolutionBase


def find_best_combination(remaining_ingredients, remaining_spoons, ingredients, recipy, calory_restriction=None):
    if remaining_spoons == 0:
        return calc_score(recipy, ingredients, calory_restriction)

    ingredient = remaining_ingredients[0]
    remaining_ingredients = remaining_ingredients[1:]

    if len(remaining_ingredients) == 0:
        recipy[ingredient] = remaining_spoons
        return find_best_combination(remaining_ingredients, 0, ingredients, recipy, calory_restriction)

    max_score = 0

    for spoons in range(remaining_spoons + 1):
        recipy[ingredient] = spoons
        score = find_best_combination(remaining_ingredients, (remaining_spoons - spoons), ingredients, recipy,
                                      calory_restriction)

        if score > max_score:
            max_score = score

    return max_score


def calc_score(recipie, ingredients, calory_restriction):
    feature_score = {
        'cap': 0,
        'dur': 0,
        'fla': 0,
        'tex': 0,
        'cal': 0,
    }

    for i in recipie:
        cap, dur, fla, tex, cal = ingredients[i]
        quantity = recipie[i]

        feature_score['cap'] += cap * quantity
        feature_score['dur'] += dur * quantity
        feature_score['fla'] += fla * quantity
        feature_score['tex'] += tex * quantity
        feature_score['cal'] += cal * quantity

    score = 1
    for key in feature_score:
        if key != 'cal':
            score *= feature_score[key] if feature_score[key] >= 0 else 0
    if calory_restriction:
        return score if feature_score['cal'] == calory_restriction else 0
    else:
        return score


def parse_input(lines):
    ingredients = {}
    for line in [l.strip() for l in lines if l]:
        result = re.search(r'(\w+): .* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+)', line)
        name, capacity, durability, flavor, texture, calories = result.groups()

        ingredients[name] = (int(capacity), int(durability), int(flavor), int(texture), int(calories))

    return ingredients


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 15)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            ing = parse_input(f.readlines())

            return find_best_combination(list(ing.keys()), 100, ing, {})

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            ing = parse_input(f.readlines())

            return find_best_combination(list(ing.keys()), 100, ing, {}, calory_restriction=500)
