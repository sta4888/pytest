from l1_function_test import square, cube


class TestClass:
    # Share our common number between test instances
    num = 5

    # Test squaring of a number
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2

    # Test cubing of a number
    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3