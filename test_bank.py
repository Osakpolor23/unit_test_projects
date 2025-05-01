# import the value function and pytest package
from bank import value
import pytest

# define test_value() function
def test_value():
    # check if hello equates zero
    assert value("hello") == 0
    # check if first letter starting with h but not hello equates 20
    assert value("hey there") == 20
    # check if other words equates 100
    assert value("what's up?") == 100
    # check for case insensitivity
    assert value("Hello") == 0