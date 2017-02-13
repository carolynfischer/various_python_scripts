"""
Below we will define what and n-interesting polygon is and your task is to find its 
area for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting 
polygon is obtained by taking the n-1 -interesting polygon and appending 1-interesting 
polygons to its rim side by side. 
"""

def shapeArea(n):
    boxes = 0
    edges = 4
    total = 1
    # sequence added: 1, 5, 13, 25
    # added: 4, 8, 12
    for i in range(0, n-1):
        boxes += edges
        total += boxes
    return total

if __name__ == "__main__":
    print shapeArea(3)