"""
Given a list, find which numbers are repeated and how many times.
"""
from collections import defaultdict


def find_repeated(elements):
    singles = []
    duplicates = defaultdict(int)

    for i in elements:
        if i not in singles:
            singles.append(i)
        else:
            duplicates[i] += 1
    return duplicates


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7]
    result = find_repeated(elements)
    for k, v in result.items():
        print "Found {} {} times".format(k, v)
