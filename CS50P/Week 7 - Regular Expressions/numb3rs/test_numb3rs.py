from numb3rs import validate

def test_validate_numeric():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False

def test_validate_letters():
    assert validate("cat") == False
    assert validate("Foo") == False
    assert validate("cat.foo.cat.foo") == False
    assert validate ("120.1.2.cat") == False
