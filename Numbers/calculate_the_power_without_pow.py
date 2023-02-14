def power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result
print(power(5, 5))