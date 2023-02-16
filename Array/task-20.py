# Python program to perform left rotation of array elements by two positions.

def left_rotate_array_by_two(arr):
    # Get the first two elements of the array
    temp = arr[:2]

    # Remove the first two elements from the array
    arr = arr[2:]

    # Add the first two elements to the end of the array
    arr.extend(temp)

    return arr

# Define an array
arr = [1, 2, 3, 4, 5]

# Perform a left rotation of the array by two positions
new_arr = left_rotate_array_by_two(arr)

# Print the new array
print(new_arr)

