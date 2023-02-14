def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

def order(x):
    if x == 0:
        return 0
    else:
        return 1 + order(x//10)

def is_armstrong(x):
    n = order(x)
    temp = x
    sum = 0
    while temp != 0:
        digit = temp % 10
        sum += power(digit, n)
        temp = temp // 10
    return (x==sum)

x = int(input("Enter a number: "))

if is_armstrong(x):
    print(x, "is an armstrong number")
else:
    print(x, "it is not an armstrong number")