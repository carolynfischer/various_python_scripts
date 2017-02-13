# beak a string without spaces to a sentence with spaces

word_list = ["peanut", "butter", "jelly", "fish", "rod"]

def split_words(word):
    so_far = ""
    sentence = ""
    for i in word:
        so_far += i
        if so_far in word_list:
            sentence += so_far + " "
            so_far = ""
    print sentence


if __name__ == "__main__":
    split_words("peanutbutterjelly")