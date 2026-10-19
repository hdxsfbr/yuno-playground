from calc import add, gcd, lcm, multiply, slugify, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0
    assert multiply(1.5, 2) == 3.0


def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(-12, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0


def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(-4, 6) == 12
    assert lcm(7, 13) == 91
    assert lcm(5, 5) == 5


def test_lcm_zero():
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    assert lcm(0, 0) == 0


def test_slugify_empty():
    assert slugify("") == ""


def test_slugify_spaces():
    assert slugify("  Hello   World ") == "hello-world"


def test_slugify_punctuation():
    assert slugify("Hi, there!! -- OK?") == "hi-there-ok"
    assert slugify("!!!") == ""
