import sys

import pytest

from l1_function_test import square, cube


@pytest.mark.skip
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2


@pytest.mark.skip
class TestClass:
    # Share our common number between test instances
    num = 5

    # Test squaring of a number
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2

    @pytest.mark.skip
    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3


def test_square_2():
    pytest.skip()
    num = 5
    result = square(num)
    assert result == num ** 2


@pytest.mark.skip(reason="Look! We are skipping this test!")
def test_square_3():
    pytest.skip()
    num = 5
    result = square(num)
    assert result == num ** 2


@pytest.mark.skipif(
    sys.version_info > (3, 6), reason="Test requires Python version <= 3.6!"
)
def test_square_4():
    num = 5
    result = square(num)
    assert result == num ** 2

def test_square_6():
    num = 5
    result = square(num)
    assert result == num ** 2

# my_import = pytest.importorskip("my_module")
def test_square_5():
    num = 5
    result = square(num)
    assert result == num ** 2

@pytest.mark.xfail
def test_square_7():
    num = 5
    result = square(num)
    assert result == num ** 2

def test_square_8():
    pytest.xfail()
    num = 5
    result = square(num)
    assert result == num ** 2

@pytest.mark.parametrize("num", [1, 2, 3, 4, 5])
def test_square8(num):
    result = square(num)
    assert result == num ** 2


@pytest.mark.parametrize("num,ref", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
def test_square8(num, ref):
    result = square(num)
    assert result == ref


@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_square9(base, exponent):
    result = square(base)
    assert result == exponent