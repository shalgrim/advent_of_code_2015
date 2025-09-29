from day20_1 import factors, calc_num_presents


def test_factors():
    assert factors(1) == {1}
    assert factors(2) == {1, 2}
    assert factors(3) == {1, 3}
    assert factors(4) == {1, 2, 4}
    assert factors(5) == {1, 5}
    assert factors(6) == {1, 2, 3, 6}
    assert factors(7) == {1, 7}
    assert factors(8) == {1, 2, 4, 8}
    assert factors(9) == {1, 3, 9}
    assert factors(10) == {1, 2, 5, 10}


def test_calc_num_presents():
    assert calc_num_presents(1) == 10
    assert calc_num_presents(2) == 30
    assert calc_num_presents(3) == 40
    assert calc_num_presents(4) == 70
    assert calc_num_presents(5) == 60
    assert calc_num_presents(6) == 120
    assert calc_num_presents(7) == 80
    assert calc_num_presents(8) == 150
    assert calc_num_presents(9) == 130
