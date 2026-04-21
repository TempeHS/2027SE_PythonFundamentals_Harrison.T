from plates import is_valid


def test_plate():
    assert is_valid("CS50") == True


def test_plater():
    assert is_valid("CS05") == False


def test_platerr():
    assert is_valid("H") == False


def test_platerrr():
    assert is_valid("OUTATIME") == False


def test_plate1():
    assert is_valid("PI3.14") == False


def test_plater2():
    assert is_valid("CS50P") == False
