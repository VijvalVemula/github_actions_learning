from src.math_operations import *

def test_add():
    assert addition(2, 3) == 5
    assert addition(-1, 3) == 2

def test_subtract():
    assert subtraction(2, 3) == -1
    assert subtraction(-1, 3) == -4

