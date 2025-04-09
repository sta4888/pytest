import pytest

from l1_function_test import square


@pytest.fixture
def initial_value():
    return 5

@pytest.fixture(autouse=True)
def log_start():
    print("Test Starting!")


# One test that uses our fixture
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2


