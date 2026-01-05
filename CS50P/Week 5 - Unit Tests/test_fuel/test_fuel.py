# Problem set: https://cs50.harvard.edu/python/psets/5/test_fuel/

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99
    try:
        convert("three/four")
    except ValueError:
        pass
    else:
        assert False
    try:
        convert("-3/4")
    except ValueError:
        pass
    else:
        assert False
    try:
        convert("4/0")
    except ZeroDivisionError:
        pass
    else:
        assert False

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
