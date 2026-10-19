from calc import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation():
    assert slugify("Hello, World! It's me.") == "hello-world-its-me"


def test_whitespace_runs_and_edges():
    assert slugify("  a   b\tc  ") == "a-b-c"


def test_empty_and_only_punctuation():
    assert slugify("") == ""
    assert slugify("!?.") == ""


def test_digits_and_existing_hyphens():
    assert slugify("Python 3-11") == "python-3-11"
