#Write a program in Python to find largest and smallest number in array.




def find_max_min(arr):
    # Initialize the maximum and minimum values to the first element in the array
    max_val = arr[0]
    min_val = arr[0]

    # Iterate over the array and update the maximum and minimum values if necessary
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    # Return the maximum and minimum values as a tuple
    return (max_val, min_val)

arr = [11, 12, 13, 14, 15, 16, 17, 18, 19]
max_val, min_val = find_max_min(arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)