"""
Print lines of a file in reverse order
"""

def print_reverse(file):
    for line in reversed(list(open(file))):
        print line

if __name__ == "__main__":
    print_reverse('hash2.py')