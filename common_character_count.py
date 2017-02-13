"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def commonCharacterCount(s1, s2):
    set1 = [x for x in s1]
    set2 = [x for x in s2]
    
    intersection = []
    for i in range(len(set1)):
        if set1[i] in set2:
            intersection.append(set1[i])
            for j in range(len(set2)):
                if set2[j] == set1[i]:
                    del set2[j]
                    break
    return len(intersection)

if __name__ == "__main__":
    print commonCharacterCount("aabcc", "adcaa")