"""
Some people are standing in a row in a park. There are trees between them 
which cannot be moved. Your task is to rearrange the people by their heights 
in a non-descending order without moving the trees.

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] 
is the height of a person standing in the ith position.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def sortByHeight(a):
    people_heights = sorted([int(x) for x in a if x != -1], reverse=True)
    new = []

    for i in range(len(a)):
        if a[i] == -1:
            new.append(-1)
        else:
            new.append(people_heights.pop())
    return new


if __name__ == "__main__":
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(sortByHeight(a))