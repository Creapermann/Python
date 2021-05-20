"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse_int(n):
    result = 0

    negativ = n < 10
    n = abs(n)

    while n > 0:
        result = int((result * 10) + (n % 10))
        n = int(n / 10)

    if negativ:
        result *= (-1)

    return result


print(reverse_int(-912))
