from twttr import shorten


def test_default():
    assert shorten("") == ""


def test_words():
    assert shorten("Twitter") == "Twttr"


def test_vowels():
    assert shorten("A") == ""
