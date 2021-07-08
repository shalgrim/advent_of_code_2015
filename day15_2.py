from collections import defaultdict

from day15_1 import parse_ingredients, score_cookie


def cookie_calories(ingredients, amounts):
    return sum([i.calories * a for i, a in zip(ingredients, amounts)])


def main(raw_ingredient_lines):
    ingredients = parse_ingredients(raw_ingredient_lines)
    max_score = 0

    for amount1 in range(101):
        for amount2 in range(101 - amount1):
            for amount3 in range(101 - (amount1 + amount2)):
                for amount4 in range(101 - (amount1 + amount2 + amount3)):
                    amounts = [amount1, amount2, amount3, amount4]
                    calories = cookie_calories(ingredients, amounts)
                    score = score_cookie(ingredients, amounts)
                    if calories == 500:
                        max_score = max(max_score, score)

    return max_score


if __name__ == '__main__':
    with open('data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))
