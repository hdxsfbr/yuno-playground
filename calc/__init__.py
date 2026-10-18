"""A small calculator module."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of a and b (Euclid)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
