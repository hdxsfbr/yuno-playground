"""A small calculator module."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def gcd(a: int, b: int) -> int:
    """Return the non-negative gcd of a and b by Euclid: replace (a, b) with (b, a % b) until b is 0."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
