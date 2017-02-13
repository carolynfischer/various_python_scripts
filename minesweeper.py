
# Write a function that generates a minesweeper grid of
# height x width with M mines in random locations.
#
# Return just the data, NO NEED TO PRINT the grid
#
# Example:
# For height 2, width 3, mines 3:
# +---+---+---+
# | X |   |   |
# +-----------+
# |   | X | X |
# +---+---+---+
import random
from collections import defaultdict
# random.randint(a, b)
# Return a random integer N such that a <= N <= b.


#10e6 x 10e6   mines 10e12 / 2


#100 50 empty 50 full
#locations = [[0,2], [2,4]]
#(y2-y1) + (x2-x1)
#0, 0
#locations = sorted(locations, key=lambda i: abs(0 - i[0]), abs(0-i[1]))

def minesweeper(height, width, mines):
    """ Minesweeper grid
    return: 
    """
    
    # [[o,x,o], [x,o,o]]
    grid = defaultdict(list)
    
    for i in xrange(height-1):
        for j in xrange(width-1):
            print grid, i, j
            grid[i] = "o"
    while mines > 0:
        randh = random.randint(0, height-1)
        randw = random.randint(0, width-1)
        if grid[randh][randw] != "x":
            grid[randh][randw] = 'x'
            mines -= 1
        
    return grid

if __name__ == "__main__":
    minesweeper(9, 3, 2)