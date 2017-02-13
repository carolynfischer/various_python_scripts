"""
Write a function answer(x), which when given a number x, returns the final digit resulting from performing the above described repeated sum process on x.
x will be 0 or greater, and less than 2^31 -1 (or 2147483647), and the answer should be 0 or greater, and a single integer digit.
"""

def answer(x):
    result = summation(x)
    while len(str(result)) > 1:
        result = summation(result)

    return result


def summation(x):
    if len(str(x)) > 1:
        sum = 0
        for i in str(x):
            sum += int(i)
    else:
        sum = x
    return sum

if __name__ == "__main__":
    print answer(1235)