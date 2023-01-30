def fibonacci_iterative(n):
    a, b = 0,1
    sum =0
    for i in range(n):
        print(sum)
        sum = a + b
        b = a
        a = sum