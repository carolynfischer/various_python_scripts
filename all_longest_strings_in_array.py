"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):
    maxlen = max([len(x) for x in inputArray])
    longest = []
    for i in inputArray:
        if len(i) == maxlen:
            longest.append(i)
    return longest

if __name__ == "__main__":
    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    print allLongestStrings(inputArray)