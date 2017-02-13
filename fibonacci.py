"""
Print n-th fibonacci number
"""
numbers = {}

def fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    elif n in numbers.keys():
        return numbers[n]
    else:
        result = fib(n-1) + fib(n-2)
        numbers[n] = result
        return result

if __name__ == "__main__":
    print fib(20)