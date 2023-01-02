# Algorithm
#     Input Integer:  number  
#     (1) Initialize variable revs_number = 0  
#     (2) Loop while number > 0  
#          (a) Multiply revs_number by 10 and add remainder of number   
#               divide by 10 to revs_number  
#                    revs_number = revs_number*10 + number%10;  
#          (b) Divide num by 10  
#     (3) Return revs_number  

# Ask for enter the number from the use  
number = int(input("Enter the Number: "))
# Method-1 string slicing

# print(f"Original number: {number}")
# reversed_number = str(number)[::-1]
# print(f"reversed number: {reversed_number}")

#Method-2 without using string reversal
print(f"Original number: {number}")
# Initiate value to null  
reverse_number = 0

# reverse the integer number using the while loop 
while number > 0:
    remainder = number % 10
    reverse_number = reverse_number*10 + remainder
    number = number // 10
    
print(f"Reversed number: {reverse_number}" )
