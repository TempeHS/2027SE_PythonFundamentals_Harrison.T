from bank import bingo


def test_hello():
    assert bingo("hello") == "$0"


def test_h():
    assert bingo("hey") == "$20"


def test_else():
    assert bingo("whatsup") == "$100"
