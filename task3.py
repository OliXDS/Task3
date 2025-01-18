def check_palindrome(word):
    word = word.lower()
    inverse = word[::-1]
    if inverse == word:
        return True
    else: 
        return False

print(check_palindrome("Kayak"))
# kayak --> inverse and check from original