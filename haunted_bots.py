"""
After becoming famous, CodeBots decided to move to a new building and live together. 
The building is represented by a rectangular matrix of rooms, each cell containing an 
integer - the price of the room. Some rooms are free (their cost is 0), but that's 
probably because they are haunted, so all the bots are afraid of them. That is why any 
room that is free or is located anywhere below a free room in the same column is not 
considered suitable for the bots.

Help the bots calculate the total price of all the rooms that are suitable for them.

Example: For
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.

Here's the rooms matrix with unsuitable rooms marked with 'x':

[[x, 1, 1, 2], 
 [x, 5, x, x], 
 [x, x, x, x]]
Thus, the answer is 1 + 5 + 1 + 2 = 9.
"""

def matrixElementsSum(matrix):
    cost = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column])
            if row == 0:
                cost += matrix[row][column]
            else:
                found = False
                for previous_row in range(row):
                    print("previous", matrix[previous_row][column])
                    if (matrix[row][column] == 0 or matrix[previous_row][column] == 0):
                        found = True
                if not found:                   
                    cost += matrix[row][column]
    print("total", cost)
    return cost

if __name__ == "__main__":
    #matrix = [[0, 1, 1, 2], 
    #          [0, 5, 0, 0], 
    #          [2, 0, 3, 3]]
    matrix = [[1,1,1,0], 
              [0,5,0,1], 
              [2,1,3,10]]
    print(matrix)
    print matrixElementsSum(matrix)