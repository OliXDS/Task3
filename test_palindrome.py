from task3 import check_palindrome


def test_is_palindrome():
    assert check_palindrome("boat") == False
    assert check_palindrome("kayak") == True
    #assert check_palindrome("Kayak") == True 
    #assert check_palindrome("ka yak") == True



# NOT A PALINDROME
# boat --> toab 

# IS A PALINDROME
# kayak --> kayak
# Kayak --> kayaK
# ka yak --> kay ak