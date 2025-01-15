""""


# initialise function
def check_palindrome(word):
    # finds the inverse of the given word
    inverse = word[::-1]
    # checks inverse is the same as the word
    if inverse == word:
        return True
    else: 
        return False



# prints and calls the function
print(check_palindrome("boat"))




def check_palindrome(word):
    if word == word[::-1]: return True

print(check_palindrome("boat"))

"""

def is_pali(word):

    return word == word[::-1]
