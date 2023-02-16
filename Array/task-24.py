# Python Program to add two number using recursion.

def add_numbers(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a

    # Recursive case: add 1 to a and subtract 1 from b, then call the function again
    return add_numbers(a + 1, b - 1)

# Add 3 and 4 using recursion
result = add_numbers(3, 4)

# Print the result
print(result)
