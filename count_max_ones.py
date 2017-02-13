"""
Count the max nr that a binary string has ones.
E.g.: 110111110001011011 => 5
"""

def count_max_ones(binary):
    max_nr = 0
    cur_batch = 0

    for i in str(binary):
        if i == "1":
            cur_batch += 1
        else:
            if cur_batch > max_nr:
                max_nr = cur_batch
            cur_batch = 0
    if cur_batch > max_nr:
        max_nr = cur_batch

    return max_nr

if __name__ == "__main__":
    print count_max_ones(110111110001011011)
    print count_max_ones(1101111100010110111111)
