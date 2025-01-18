def check_palindrome(word):
    inverse = word[::-1]
    if inverse == word:
        return True
    else: 
        return False

print(check_palindrome("kayak"))
# kayak --> inverse and check from original