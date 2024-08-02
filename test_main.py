"""this is the test file for the main module
    """

from main import runner


def test_random_func():
    """this the test funtion to tes tthe our package from random module"""
    val = runner()
    assert val == 0
