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

    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if A[i] == B[i]:
            continue
        else:
            for j in range(i, len(B)):
                # found, flip and continue
                if A[i] == B[j]:
                    B[i], B[j] = B[j], B[i]
                    faults += 1
                    if faults > 1:
                        print(A, B), faults
                        return False
                    break
            if A[i] != B[i]:         
                print(A, B)     
                return False
    print(A, B)
    return True

"""
def areSimilar(A, B):
    ids = []
    for i in range(len(A)):
        if A[i] != B[i]:
            ids.append(i)
    if len(ids) == 0:
        return True
    if len(ids) >= 2:
        return False
    id1 = ids[0]
    id2 = ids[1]
    if A[id1] == B[id2] and A[id2] == B[id1]:
        return True
    return False
"""

if __name__ == "__main__":
    # False
    A = [1, 2, 2]
    B = [2, 1, 1]
    print(areSimilar(A, B))

    # True
    A = [1, 2, 3]
    B = [1, 2, 3]
    print(areSimilar(A, B))

    # True
    A = [1, 2, 3]
    B = [2, 1, 3]
    print(areSimilar(A, B))    

    # False
    A = [1, 2, 4]
    B = [2, 1, 3]
    print(areSimilar(A, B))     

    # False
    A = [1, 2, 1]
    B = [2, 1, 3]
    print(areSimilar(A, B)) 

    # True
    A = [3, 1, 2]
    B = [2, 1, 3]
    print(areSimilar(A, B))     

    # False
    A = [3, 12, 2]
    B = [12, 2, 3]
    print(areSimilar(A, B)) 

    # True
    A = [3, 12, 2]
    B = [3, 2, 12]
    print(areSimilar(A, B))          

    # False
    A = [2, 12, 2]
    B = [12, 2, 12]
    print(areSimilar(A, B)) 

    # False
    A = [12, 2, 3, 4]
    B = [12, 4, 2, 3]
    print(areSimilar(A, B)) 