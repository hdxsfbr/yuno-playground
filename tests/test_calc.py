import pytest

from calc import add, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0
    assert multiply(1.5, 2) == 3.0


def test_power_positive():
    assert power(2, 3) == 8


def test_power_zero():
    assert power(5, 0) == 1
    assert power(0, 0) == 1


def test_power_negative():
    assert power(2, -2) == 0.25
    with pytest.raises(ZeroDivisionError):
        power(0, -1)
