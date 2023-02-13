def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter your number: "))

if n < 0:
    print("please enter positive number")
else:
    print("fibonacci sequence is: ")
    for i in range(n):
        print(fibonacci_recursive(i))