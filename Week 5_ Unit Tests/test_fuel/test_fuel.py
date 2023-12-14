from fuel import convert, gauge
from pytest import raises

def test_convert():
    assert convert("5/5") == 100
    assert convert("5/7") == 71
    assert convert("0/5") == 0

    with raises(ValueError):
        convert("7/5")
    with raises(ZeroDivisionError):
        convert("8/0")
    with raises(ValueError):
        convert("yes.")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(45) == "45%"
    assert gauge(69) == "69%"

