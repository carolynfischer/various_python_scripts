"""
Throw a 6-sided die.
"""

import random

def throw():
    number = random.randint(1, 6)
    return number

if __name__ == "__main__":
    print throw()