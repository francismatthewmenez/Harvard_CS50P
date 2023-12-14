from plates import is_valid

def test_1():
    assert is_valid("00CS50") == False

def test_2():
    assert is_valid("EMINEM") == True

def test_3():
    assert is_valid("BC1871") == True

def test_4():
    assert is_valid("PI3.14") == False

def test_5():
    assert is_valid("H") == False

def test_6():
    assert is_valid("BC190V") == False

def test_7():
    assert is_valid("NO0123") == False

def test_8():
    assert is_valid("454325") == False


