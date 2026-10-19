import pytest

from calc import fibonacci


def test_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_sequence():
    assert [fibonacci(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_large():
    assert fibonacci(90) == 2880067194370816120


def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)
