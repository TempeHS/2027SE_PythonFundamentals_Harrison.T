from fuel import convert


def test_full():
    assert convert("5/5") == "F"


def test_empty():
    assert convert("0/5") == "E"


def test_anything():
    assert convert("3/6") == "50%"
    assert convert("5/11") == "45%"
