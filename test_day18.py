from day18_1 import make_grid
from day18_2 import make_stuck_grid


def test_day18_1():
    grid = make_grid('data/test18.txt')
    assert grid.number_on == 15

    for _ in range(4):
        grid.tick()

    assert grid.number_on == 4


def test_day18_2():
    grid = make_stuck_grid('data/test18.txt')
    assert grid.number_on == 17

    for _ in range(5):
        grid.tick()

    assert grid.number_on == 17
