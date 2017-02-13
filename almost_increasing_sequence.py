"""
Given a sequence of integers, check whether it is possible to obtain a strictly increasing sequence by erasing no more than one element from it.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;
For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.
"""

def almostIncreasingSequence(sequence):
    removed = 0
    smallest = sequence[0]
    for i in range(len(sequence)-1):   
        if sequence[i] >= sequence[i+1]:
            if removed == 0:
                removed += 1
            else:
                return False
    return True
            
if __name__ == "__main__":
    print(almostIncreasingSequence([1,3,2,1]))