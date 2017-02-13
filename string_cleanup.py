"""
For example, if the final chunk of text was "lolol," and the inserted word was "lol," the shortest possible strings are "ol" (remove "lol" from the beginning) 
and "lo" (remove "lol" from the end). The original text therefore must have been "lo," the lexicographically earliest string.

Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest string that can be formed by removing occurrences of word from 
chunk. Keep in mind that the occurrences may be nested, and that removing one occurrence might result in another. For example, removing "ab" from "aabb" results 
in another "ab" that was not originally present. Also keep in mind that your spy's original message might have been an empty string.

chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of characters in chunk.
"""

def answer(chunk, word):
    print chunk
    if chunk == "":
        return ""
    chunk = chunk[::-1]
    while word[::-1] in chunk or :
        print word[::-1]
        chunk = chunk.replace(word[::-1], "")
    return chunk[::-1]

if __name__ == "__main__":
    print answer('llolol', 'lol')