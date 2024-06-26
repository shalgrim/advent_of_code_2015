import pytest

from day19_1 import main
from day19_2 import main as main2


@pytest.fixture
def tst_input():
    with open("data/test19.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def tst_input2():
    with open("data/test19_2.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def tst_input2_2():
    with open("data/test19_2_2.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open("data/input19.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_day19_1():
    assert main('data/test19.txt') == 7
    assert main('data/input19.txt') == 535


def test_day19_2(tst_input2, tst_input2_2):
    assert main2(tst_input2) == 3
    assert main2(tst_input2_2) == 6
