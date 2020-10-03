from calc.calculator import Calculator
import pytest

def test_add():
    cal = Calculator()
    with pytest.raises(Exception):
        assert cal.add('du', 43) == 66

def test_subbstractor():
    cal = Calculator()
    assert cal.substractor(43, 23) == 20

def test_multiplay():
    cal = Calculator()
    assert cal.multiplay(2, 4) == 8

def test_divide():
    cal = Calculator()
    assert cal.divide(8.00, 4.00) == 2

def test_power():
    cal = Calculator()
    assert cal.power(3, 2) == 9