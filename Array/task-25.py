# Python Program to find sum of digit of number using recursion.

def sum_of_digits(n):
    # Base case: if n is less than 10, return n
    if n < 10:
        return n

    # Recursive case: add the last digit to the sum of the other digits
    return n % 10 + sum_of_digits(n // 10)


# Find the sum of the digits of the number 1234
result = sum_of_digits(1234)

# Print the result
print(result)
