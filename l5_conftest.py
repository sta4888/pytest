# A simple example using conftest with test fixtures
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2