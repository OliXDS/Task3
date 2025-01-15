from task3 import is_pali


def test_pytest():
    assert 2+2 == 4

def test_is_pali_happy():
    assert is_pali("radar") == True
    assert is_pali("Radar") == False