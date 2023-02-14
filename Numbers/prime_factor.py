
def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n%i == 0:
            n = n//i
            factors.append(i)
        else:
            i += 1
    if n>1:
        factors.append(n)
    return factors

num = 84
print(prime_factors(num))


