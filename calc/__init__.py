"""A small calculator module."""


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
    """Return text lowercased, with punctuation stripped and whitespace runs turned into single hyphens."""
    cleaned = "".join(c for c in text.lower() if c.isalnum() or c.isspace() or c == "-")
    return "-".join(cleaned.split())
