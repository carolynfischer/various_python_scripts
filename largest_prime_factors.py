"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import operator

def largest_prime(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

if __name__ == "__main__":
    print largest_prime(600851475143)