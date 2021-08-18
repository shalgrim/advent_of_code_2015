from day18_1 import make_grid


def test_day18_1():
    grid = make_grid('data/test18.txt')
    for _ in range(4):
        grid.tick()

    assert grid.number_on == 4
