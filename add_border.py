"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def addBorder(picture):
    result = []
    length = len(picture[0])
    full_row = "*" * length + "**"
    result.append(full_row)
    for i in range(len(picture)):
        result.append("*" + picture[i] + "*")
    result.append(full_row)
    return result

if __name__ == "__main__":
    print(addBorder(["abc", "ded"]))