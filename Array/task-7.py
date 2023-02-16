def find_top_two_max(arr):
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

    # Return the top two maximum values as a tuple
    return (max_val, second_max_val)

arr = [3, 2, 8, 5, 1, 7, 4, 6]
top_two_max = find_top_two_max(arr)
print("Top two maximum values:", top_two_max)
