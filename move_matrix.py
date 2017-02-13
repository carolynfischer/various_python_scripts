"""
Given a matrix 5x5,
find where you end up if a string is rflfbrf
"""

def move_matrix(string, n):
    row = 0
    col = 0
    direction = "right"

    
    for i in string:
        print i
        if i == "r":
            if direction == "right":
                col += 1
                direction = "down"
            elif direction == "down":
                row -= 1
                direction = "left"
            elif direction == "left":
                col -= 1
                direction = "up"
            elif direction == "up":
                row += 1
                direction = "right"
        elif i == "l":
            if direction == "right":
                col -= 1
                direction = "up"
            elif direction == "down":
                row += 1
                direction = "right"
            elif direction == "left":
                col += 1
                direction = "down"
            elif direction == "up":
                row -= 1
                direction = "left"
        elif i == "b":
            if direction == "right":
                row -= 1
            elif direction == "down":
                col -=1
            elif direction == "left":
                row += 1
            elif direction == "up":
                col += 1
        elif i == "f":
            if direction == "right":
                row += 1
            elif direction == "down":
                col += 1
            elif direction == "left":
                row -= 1
            elif direction == "up":
                col -= 1

        if col < 0 or row < 0 or row > n or col > n:
            return "Navigated off, {} {}".format(row, col)

    return (row, col)

def move_matrix2(string, n):
        r = {"right": (0, 1, "down"), "down": (-1, 0, "left"), "left": (0, -1, "up"), "up": (1, 0, "right")}
        l = {"right": (0, -1, "up"), "down": (1, 0, "right"), "left": (0, 1, "down"), "up": (-1, 0, "up")}
        b = {"right": (-1, 0, "right"), "down": (0, -1, "down"), "left": (1, 0, "left"), "up": (0, 1, "up")}
        f = {"right": (1, 0, "right"), "down": (0, 1, "down"), "left": (-1, 0, "left"), "up": (0, -1, "up")}

        row = 0
        col = 0
        direction = "right"

        for i in string:
            if i == "r": s = r
            elif i == "l": s = l
            elif i == "b": s = b
            elif i == "f": s = f
            row += s[direction][0]
            col += s[direction][1]
            direction = s[direction][2]

            if col < 0 or row < 0 or row > n or col > n:
                return "Navigated off, {} {}".format(row, col)
        return (row, col)

if __name__ == "__main__":
    print move_matrix("rfflffbrlf", 4)
    print move_matrix2("rfflffbrlf", 4)