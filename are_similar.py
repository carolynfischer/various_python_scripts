"""
Two arrays are called similar if one can be obtained from another 
by swapping at most one pair of elements.
Given two arrays, check whether they are similar.

Example
For A = [1, 2, 3] and B = [1, 2, 3], the output should be
areSimilar(A, B) = true;
For A = [1, 2, 3] and B = [2, 1, 3], the output should be
areSimilar(A, B) = true;
For A = [1, 2, 2] and B = [2, 1, 1], the output should be
areSimilar(A, B) = false.
"""

def areSimilar(A, B):
    faults = 0

    for i in range(len(A)):
        if A[i] == B[i]:
            continue
        else:
            if faults > 0:
                return False
            else:
                match = ""
                for j in range(i, len(B)):
                    # found, flip and continue
                    if A[i] == B[j]:
                        B[i], B[j] = B[j], B[i]
                        faults += 1
                        if faults > 1:
                            return False
                        match = B[j]
                        break
                if match and A[i] == B[i]:
                    continue
                else:
                    return False
    return True

if __name__ == "__main__":
    A = [1, 2, 2]
    B = [2, 1, 1]
    print(areSimilar(A, B))

    A = [1, 2, 3]
    B = [1, 2, 3]
    print(areSimilar(A, B))

    A = [1, 2, 3]
    B = [2, 1, 3]
    print(areSimilar(A, B))    