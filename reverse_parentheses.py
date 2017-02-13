"""
You are given a string s that consists of English letters, punctuation 
marks, whitespace characters and brackets. It is guaranteed that the 
brackets in s form a regular bracket sequence.

Your task is to reverse the strings in each pair of matching parenthesis, 
starting from the innermost one.

Example
For string "s = a(bc)de" the output should be
reverseParentheses(s) = "acbde".

s: "Code(Cha(lle)nge)"
Expected Output:
"CodeegnlleahC"

s: "a(bcdefghijkl(mno)p)q"
Expected Output:
"apmnolkjihgfedcbq"

"""

def reverseParentheses(s):
    new = [str(x) for x in s]
    ends = []
 
    while True:
        start = s.find("(") 
        starts = []
        starts.append(start)
        while start != -1:
            start = s.find("(", start+1)
            starts.append(start)
        if len(starts) == 1:
            break
        else:
            start = starts[-2]

        end = s.find(")", start)
        new[start:end+1] = s[start+1:end][::-1]
        s = "".join(new)
    return s


if __name__ == "__main__":
    print(reverseParentheses("a(bcdefghijkl(mno)p)q"))
    print("apmnolkjihgfedcbq")

    print(reverseParentheses("Code(Cha(lle)nge)"))
    print("CodeegnlleahC")
    print()

    print(reverseParentheses("co(de(fight)s)"))
    print("cosfighted")