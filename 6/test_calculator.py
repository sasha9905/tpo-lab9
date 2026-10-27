import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (0, 0, 0), (-1, 5, 4), (100, -40, 60)],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 2, 5), (9, 3, 3), (-8, 2, -4)],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.mark.parametrize(
    "n,expected",
    [(2, True), (3, True), (4, False), (1, False), (0, False), (17, True), (15, False)],
)
def test_is_prime(calc, n, expected):
    assert calc.is_prime_number(n) is expected
