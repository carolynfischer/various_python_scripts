"""
Compress string "aabcaaaaade" to "aabc5xade". Only compress if it shortens the string. 5xa means char a is repeated 5 times.
"""

def minify(s):
    so_far = []
    new_string = ""
    for i in range(len(s)):
        # there was a previous letter and it matched the current letter - let's append to list
        if so_far and s[i] == so_far[0]:
            so_far.append(s[i])
        # there was a previous letter and the current letter was not the same - flush out
        elif so_far and s[i] != so_far[0]:
            if len(so_far) > 3:
                new_string += str(len(so_far)) + "x" + so_far[0]
            else:
                new_string += "".join(so_far)
            so_far = [s[i]]
        elif not so_far:
            so_far.append(s[i])

    new_string += "".join(so_far)
    return new_string

if __name__ == "__main__":
    print minify('aabcaaaaade')