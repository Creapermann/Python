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