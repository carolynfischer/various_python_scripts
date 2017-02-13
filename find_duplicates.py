"""
write a function that finds duplicate files after a malicious attack
"""

import os
from os.path import join

def find_duplicates(dirpath):
    files_list = []
    duplicates = []

    for root, dirs, files in os.walk(dirpath, topdown=True):
        for name in files:
            if name not in files_list:
                files_list.append(name)
            else:
                duplicates.append(join(root, name))

    return duplicates

if __name__ == "__main__":
    print find_duplicates("/home/carry/Documents/eBooks")
