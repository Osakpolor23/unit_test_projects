# import the functions and packages
from plates import is_valid
import pytest

# define the test_is_valid() function
def test_is_valid():
    # check for correct length, begins with letters, correct number placement
    assert is_valid("CS5032") == True
    # check for letters starting plates
    assert is_valid("32458") == False
    # check for zero not being the first digit
    assert is_valid("Os0325") == False
    # check for incorrect letter placement after digits
    assert is_valid("Osa1960P") == False
    # check for correct length, begins with letters, correct number placement
    assert is_valid("Os1960") == True
    # # check for correct length, begins with letters, correct number placement (case insensitivity)
    assert is_valid("os2025") == True
    # check for length
    assert is_valid("o") == False
    # check for number placement
    assert is_valid("AAA22P") == False
    # check for alphanumeric condition(i.e contains no symbols or special characters except numbers and letters)
    assert is_valid("os_224") == False