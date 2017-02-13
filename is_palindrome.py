"""
is_palindrome - check if a string is a palindrome
"""

def is_palindrome(s1, s2):
    word1 = sorted(to_list(s1))
    word2 = sorted(to_list(s2))

    if word1 == word2 :
        return True
    else:
        return False
    
def to_list(s):
    word = []
    for i in s:
        word.append(i)
    return word

if __name__ == "__main__":
    print is_palindrome("taco cat", "octa cat")
    print is_palindrome("octa", "cat")