import re
from dataclasses import dataclass
from typing import List

pattern = re.compile(
    r'^\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$'
)


@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse_ingredients(raw_ingredient_lines):
    answer = [
        Ingredient(*[int(g) for g in pattern.match(line).groups()])
        for line in raw_ingredient_lines
    ]
    return answer


def score_cookie(ingredients: List[Ingredient], amounts: List[int]):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i, a in zip(ingredients, amounts):
        capacity += i.capacity * a
        durability += i.durability * a
        flavor += i.flavor * a
        texture += i.texture * a

    return max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)


def main(raw_ingredient_lines):
    ingredients = parse_ingredients(raw_ingredient_lines)
    max_score = 0
    for amount1 in range(101):
        for amount2 in range(101 - amount1):
            for amount3 in range(101 - (amount1 + amount2)):
                for amount4 in range(101 - (amount1 + amount2 + amount3)):
                    max_score = max(max_score, score_cookie(ingredients, [amount1, amount2, amount3, amount4]))
    return max_score


if __name__ == '__main__':
    with open('data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))
