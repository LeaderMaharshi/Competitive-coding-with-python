# In number theory, a perfect number is a positive integer that is equal to the sum of its proper
# divisors (excluding the number itself). Here's an example code in Python to determine whether
# a given number is perfect or not:

def perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

print(perfect_number(6))