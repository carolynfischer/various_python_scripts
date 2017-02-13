"""
given two strings, write a method to decide if one is permutation of the other
"""

def is_permutation(s1, s2):
    word1 = sorted(to_list(s1))
    word2 = sorted(to_list(s2))
    if word1 == word2:
        return True
    else:
        return False


def to_list(s):
    word = []
    for i in s:
        word.append(i)
    return word

if __name__ == "__main__":
    print is_permutation('kalapala', 'palakala')
    print is_permutation('kala', 'pala')