

def is_prime(num):
    if num <= 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_in_range(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)

prime_in_range(1, 100)