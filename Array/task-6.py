# Write a program in Python to find second highest number in an integer array.

def find_second_highest(arr):
    # Initialize the maximum and second maximum values to the smallest integer possible
    max_val = float('-inf')
    second_max_val = float('-inf')

    # Iterate over the array and update the maximum and second maximum values if necessary
    for i in range(len(arr)):
        if arr[i] > max_val:
            second_max_val = max_val
            max_val = arr[i]
        elif arr[i] > second_max_val:
            second_max_val = arr[i]

    # Return the second maximum value
    return second_max_val

arr = [3, 2, 8, 5, 1, 7, 4, 6]
second_max_val = find_second_highest(arr)
print("Second highest value:", second_max_val)
