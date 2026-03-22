from jar import Jar
import pytest

def test_init():
    jar1 = Jar()
    assert jar1.size == 0
    assert jar1.capacity == 12

    jar2 = Jar(24)
    assert jar2.capacity == 24

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.size == 0

    jar.deposit(10)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(10)
