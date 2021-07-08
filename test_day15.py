from day15_1 import Ingredient, parse_ingredients, score_cookie
from day15_2 import cookie_calories

TEST_LINES = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
]


def test_parse_ingredients():
    assert parse_ingredients(TEST_LINES) == [
        Ingredient(-1, -2, 6, 3, 8),
        Ingredient(2, 3, -2, -1, 3),
    ]


def test_score_cookie():
    ingredients = parse_ingredients(TEST_LINES)
    amounts = [44, 56]
    assert score_cookie(ingredients, amounts) == 62842880


def test_cookie_calories():
    ingredients = parse_ingredients(TEST_LINES)
    amounts = [40, 60]
    assert cookie_calories(ingredients, amounts) == 500
