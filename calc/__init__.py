"""A small calculator module."""

import re


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of a and b."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the non-negative least common multiple of a and b (0 if either is 0)."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def slugify(text: str) -> str:
    """Return text lowercased with runs of non-alphanumerics as single hyphens, trimmed."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
