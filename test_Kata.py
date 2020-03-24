from Kata import Add

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