n = input("Enter a number: ")

reverse = str(n[::-1])

if n == reverse:
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome number")