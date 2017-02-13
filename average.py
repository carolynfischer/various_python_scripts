"""
Average the 4th column in a csv file that has 100000 lines
"""
import statistics

def average(file):
    entries = []
    with open(file, 'r') as f:
        line = f.readline()
        if line:
            entries.append(int(line.split(",")[3]))
    return statistics.mean(entries)

if __name__ == "__main__":
    print average("100k.csv")