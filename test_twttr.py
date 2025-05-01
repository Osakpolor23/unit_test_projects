# import the shorten function and pytest package
from twttr import shorten
import pytest


# define test_shorten() function
def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HellO") == "Hll"
    assert shorten("twitter") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

