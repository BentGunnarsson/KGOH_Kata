from Kata import Add
import pytest

def test_add_nothing():
    assert Add("") == 0

def test_add_one_number():
    assert Add("3") == 3

def test_add_two_numbers():
    assert Add("3,7") == 10

def test_add_unknown_amt_of_numbers():
    assert Add("3,7,14,11,2") == 37

def test_add_with_newline_delimiter():
    assert Add("1\n2,3") == 6

def test_ignore_above_1000():
    assert Add("1001,4") == 4

def test_negatives_exception():
    with pytest.raises(Exception):
        assert Add("-2,4,-5,-7") == "No negatives allowed: -2,-5,-7"