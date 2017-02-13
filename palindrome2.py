"""
Check if a string is a palindrome
"""

def palindrome(string):
    if string == string[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

if __name__ == "__main__":
    print palindrome('kalapala')
    print palindrome('aias sadas sai)'