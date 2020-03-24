from Kata import Add

def test_add_nothing():
    assert Add("") == 0

def test_add_one_number():
    assert Add("3") == 3

def test_add_two_numbers():
    assert Add("3,7") == 10