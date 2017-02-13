"""
Write a function called answer(x) that returns the maximum number of minion employees a company following the "no more than 7 direct reports" theory can have, 
with no more than x levels of supervision.

You can assume that:
1. Professor Boolean is the highest level of supervision and has no manager.
2. Each minion employee (other than Professor Boolean) has exactly one manager.

For example, with no more than 1 level of supervision, we could have a maximum of 8 employees: Professor Boolean and his 7 reports.

x will be a positive integer, not exceeding 10.
"""

def answer(x):
    minions = 1
    last = 7
    for i in range(x, 0, -1):
        last = 7 ** i
        minions += last
    
    return minions

if __name__ == "__main__":
    print answer(4)