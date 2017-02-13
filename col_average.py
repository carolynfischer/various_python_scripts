"""
Calculate the third column of a csv file
Python2.7
"""
import os
import random


def generate_data(csv_file):
    """
    Generate a csv file with 5 columns, filled with random integers from 1 to 100
    """
    columns = 5
    rows = 100000

    with open(csv_file, 'w') as f:
        for _ in range(rows):
            line = ""
            for i in range(columns):
                line += str(random.randint(1, 100))
                if i != columns-1:
                    line += "," 
                else:
                    line += "\n"
            f.write(line)


def calculate(csv_file):
    total = 0
    # in this case it will be 100 000, but in other cases may vary, so checking
    items = 0  

    with open(csv_file, 'r') as f:
        for line in f.readlines():
            line = line[:-1]
            third = line.split(",")[2]
            total += int(third)
            items += 1
    print total, items
    result = float(total) / items
    return result

if __name__ == "__main__":
    csv_file = "data.txt"
    os.remove(csv_file)
    generate_data(csv_file)
    print calculate(csv_file)
