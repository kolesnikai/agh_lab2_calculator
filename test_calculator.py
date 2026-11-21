from math import isnan
from calculator import Calculator


def test_pierwsza_wartosc():
    kalkulator = Calculator(5.0, 3.0)

    assert kalkulator.op1 == 5.0


def test_druga_wartosc():
    kalkulator = Calculator(5.0, 3.0)

    assert kalkulator.op2 == 3.0


def test_sum():
    kalkulator = Calculator(10.0, 2.0)

    assert kalkulator.sum() == 12.0


def test_subtract():
    kalkulator = Calculator(10.0, 2.0)

    assert kalkulator.subtract() == 8.0


def test_multiply():
    kalkulator = Calculator(10.0, 2.0)

    assert kalkulator.multiply() == 20.0


def test_divide():
    kalkulator = Calculator(10.0, 2.0)

    assert kalkulator.divide() == 5.0

def test_divide_zero():
    kalkulator= Calculator(5.0,0.0)
    assert isnan(kalkulator.divide())


