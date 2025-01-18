# check if input is a palindrome 
def check_palindrome(word):
    # converts all characters to lowercase
    word = word.lower()


    # stores the inverse of word
    inverse = word[::-1]
    # checks is inverse is equal to the word
    if inverse == word:
        return True
    # if word is not equal to the inverse then return False
    else: 
        return False


# calling the function and passing a parameter
print(check_palindrome("Ka yak"))


