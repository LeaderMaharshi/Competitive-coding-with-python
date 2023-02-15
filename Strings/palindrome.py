string = "racecar"

# Removing spaces and converting to lowercase
string = string.replace(" ", "").lower()

# Reversing the string using slicing
reverse_string = string[::-1]

# Comparing the original and reversed strings
if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
