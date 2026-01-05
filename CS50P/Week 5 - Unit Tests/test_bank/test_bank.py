# Problem set: https://cs50.harvard.edu/python/psets/5/test_bank/

from bank import value

def test_value():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("") == 100
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("Hello how are you?") == 0
    assert value("Good morning how are you?") == 100

# pip install pytest
# pytest test_bank.py
