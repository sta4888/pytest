from l1_function_test import *

# Tests start with "test_"
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2


# Define another test in the same file
def test_cube():
    num = 5
    result = cube(num)
    assert result == num ** 3


