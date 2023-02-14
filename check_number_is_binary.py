
def is_binary(num):
    for i in str(num):
        if i != '0' and i!= '1':
            return False
    return True

num = input("Enter the number: ")

if is_binary(num):
    print('It is binary number')
else:
    print("It is not a binary number")
