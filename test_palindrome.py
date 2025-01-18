from task3 import check_palindrome


def test_pytest():
    assert 2+2 == 4

def test_is_pali_happy():
    assert check_palindrome("radar") == True
    assert check_palindrome("Radar") == False