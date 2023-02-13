


number = int(input("Enter the Number: "))
# Method-1 string slicing

# print(f"Original number: {number}")
# reversed_number = str(number)[::-1]
# print(f"reversed number: {reversed_number}")

#Method-2 without using string reversal
print(f"Original number: {number}")

reverse_number = 0


while number > 0:
    remainder = number % 10
    reverse_number = reverse_number*10 + remainder
    number = number // 10
    
print(f"Reversed number: {reverse_number}" )
