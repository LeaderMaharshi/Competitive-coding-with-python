# Python program to perform right rotation in array by 2 positions.

def right_rotation(arr):

    temp = arr[-2:]
    arr = arr[:-2]

    arr = temp + arr

    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Perform a right rotation of the array by two positions
new_arr = right_rotation(arr)

# Print the new array
print(new_arr)

