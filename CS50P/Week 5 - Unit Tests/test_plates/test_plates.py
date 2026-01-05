# Problem set: https://cs50.harvard.edu/python/psets/5/test_plates/

from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("C50") == False

# pip install pytest
# pytest test_plates.py
