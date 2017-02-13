"""
urlify - replace all characters in a string with %20
"""

def urlify(s):
    split_string = s.split(" ")
    return "%20".join(split_string)

if __name__ == "__main__":
    print urlify("hi, my name is carolyn")