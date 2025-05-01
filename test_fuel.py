# import the functions and packages
from fuel import convert, gauge
import pytest

# define test_convert funcction
def test_convert():
    # make the assertions
    assert convert("2/3") == 67
    assert convert("1/2") == 50
    # check if these activities would raise the necessary exception errors
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

# define test_guage function
def test_guage():
    # make the assertions
    assert gauge(1) == "E"
    assert gauge(3) == "3%"
    assert gauge(67) == "67%"
    assert gauge(99) == "F"
