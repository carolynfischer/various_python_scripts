"""
Find the 5 most occurring words in a text file
"""
from collections import defaultdict

def n_most_frequent(textfile, n):
    words = defaultdict(int)
    with open(textfile, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        for word in line.split(" "):
            if word.isalpha():
                words[word] += 1
    words = sorted(words.items(), key=lambda(k,v): v, reverse=True)

    most_popular = []
    for i in range(n):
        most_popular.append(words[i])
    return most_popular


if __name__ == "__main__":
    print n_most_frequent("techsisters.txt", 5)