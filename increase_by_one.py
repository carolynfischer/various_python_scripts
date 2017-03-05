"""
You are given an array of integers. On each move you are allowed to 
increase exactly one of its element by one. Find the minimal number 
of moves required to obtain a strictly increasing sequence from the 
input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""

def arrayChange(inputArray):
    changes = 0
    for i in range(len(inputArray)):
        if i < len(inputArray)-1:
            if inputArray[i] < inputArray[i+1]:
                continue
            else:
                diff = inputArray[i] - inputArray[i+1]
                if diff == 0:
                    changes += 1
                    inputArray[i+1] += 1
                else:
                    changes += diff + 1
                    inputArray[i+1] += diff + 1
    return changes

if __name__ == "__main__":
    inputArray = [1, 1, 1]
    print(arrayChange(inputArray))
