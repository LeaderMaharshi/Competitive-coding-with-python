number = int(input("Enter the number: "))


def reverse(n):
    if n < 10:
        return n
    else:
        return int(str(n%10) + str(reverse((n//10))))


def is_palindrome(n):
    if number == reverse(n):
        return True
    return False

if is_palindrome(number):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
