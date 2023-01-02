# What is Armstrong Number?

#     It is a number which is equal to the sum of cube of its digits.
#     For eg: 153, 370 etc.

# Lets see it practically by calculating it,

# Suppose I am taking 153 for an example 

# First calculate the cube of its each digits

#   1^3 = (1*1*1) = 1

#   5^3 = (5*5*5) = 125

#   3^3= (3*3*3) = 27

# Now add the cube 

#   1+125+27 = 153

# It means 153 is an Armstrong number.

number = int(input("Enter a number:"))
temp = number
sum = 0
while number > 0:
    digit = number % 10
    cube = digit * digit * digit
    sum += cube
    number = number // 10


if temp == sum:
    print(f"Given number {temp} is an Amstrong Number")
else:
    print(f"Given number {temp} is not an Amstrong Number")
    
