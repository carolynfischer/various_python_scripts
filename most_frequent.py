"""
Find the 5 most occurring words in a text file
"""
from collections import defaultdict

def five_most_frequent(textfile):
    words = defaultdict(int)
    with open(textfile, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        for word in line.split(" "):
            if word.isalpha():
                words[word] += 1
    words = sorted(words.iteritems(), key=lambda(k,v): v, reverse=True)
    print words

    for i in range(5):
        print words[i]


if __name__ == "__main__":
    five_most_frequent("techsisters.txt")