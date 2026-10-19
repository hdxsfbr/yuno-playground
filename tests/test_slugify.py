from calc import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_whitespace_runs_and_edges():
    assert slugify("  a   b  ") == "a-b"


def test_empty_and_only_punctuation():
    assert slugify("") == ""
    assert slugify("?!.") == ""


def test_keeps_digits_and_hyphens():
    assert slugify("Python 3 is well-known") == "python-3-is-well-known"
