"""
Determine if all characters in the sting are unique
"""

def is_unique(s):
    split_string = []
    for i in s:
        split_string.append(i)
    unique_set = set(split_string)
    if len(s) == len(unique_set):
        return True
    else:
        return False


if __name__ == "__main__":
    print is_unique("kalapala")
    print is_unique("aoeui")