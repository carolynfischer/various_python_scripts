"""
Count words in a file, print 5 most frequent
"""
from collections import defaultdict
from operator import itemgetter

lines = []
words = defaultdict(int)

def count_words(filename):
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.rstrip("\n"))
        for line in lines:
            line = line.split()
            for word in line:
                words[word] += 1
    words_sorted = sorted(words.items(), key=itemgetter(1), reverse=True)[:5]
    return words_sorted

if __name__ == "__main__":
    print count_words('techsisters.txt')